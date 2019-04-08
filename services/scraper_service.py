import requests
import time
from bs4 import BeautifulSoup
from services import ObjectManager

def scrape_websites(user_settings, website_data, current_page, cache):
    all_clothes = []
    for website in user_settings.websites:
        cache_key = f"{website}{user_settings.gender}{user_settings.category}{current_page}"
        clothes = cache.get(cache_key)
        if clothes is None:
            object_manager = ObjectManager()
            website_settings = object_manager.get(website_data, 'website_id', website)
            clothes = scrape_website(website_settings, current_page)
            cache.set(cache_key, clothes, timeout=86400)

        all_clothes = all_clothes + clothes

    return all_clothes

# website_settings: scraper_config, url, base_url
def scrape_website(website_settings, current_page):
    clothes = []
    config = website_settings['scraper_config']
    page_html = get_html(website_settings['url'], current_page)
    for product in page_html.find_all(config['container']['tag'], class_=config['container']['class']):
        clothes.append({
            'price': product.span.text if config.get('price') is None else product.find(config['price']['tag'], class_=config['price']['class']).text,
            'img': product.img['src'] if config.get('img') is None else get_image_url(product, config),
            'name': product.h2.text if config.get('name') is None else product.find(config['name']['tag'], class_=config['name']['class']).text,
            'link': website_settings['base_url'] + product.find('a')['href'] if config.get('link') is None else website_settings['base_url'] + product.find(config['link']['tag'], class_=config['link']['class'])['href']
        })
        
    return clothes

def get_image_url(product, config):
    try:
        product_image = product.find(config['img']['tag'], class_=config['img']['class']).img
        return product_image['src']
    except KeyError:
        return product_image['data-src']   

def get_html(url, current_page):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    page_text = requests.get(url + current_page, headers=headers).text
    return BeautifulSoup(page_text, 'lxml')