import requests
import time
from bs4 import BeautifulSoup
from services import ObjectManager

def scrape_websites(user_settings, website_data, current_page):    
    data = []
    for website in website_data:
        if website.get('website_id') in user_settings.websites and website.get('gender') == user_settings.gender and website.get('category') == user_settings.category:
            data = data + scrape_website(user_settings, website, current_page)
    return data

def scrape_website(user_settings, website, current_page):
    object_manager = ObjectManager()
    page = object_manager.get(website.get('data'), 'page', current_page)

    # page content exists and has not expired
    if page is not None and time.time() - page.get('expiry') < 86400:
        return page.get('clothes')

    data = {}
    data['page'] = current_page
    data['expiry'] = time.time()
    data['clothes'] = []
    config = website['scraper_config']
    for product in get_html(website.get('url'), current_page).find_all(config['container']['tag'], class_=config['container']['class']):
        data['clothes'].append({
            'price': product.span.text if config.get('price') is None else product.find(config['price']['tag'], class_=config['price']['class']).text,
            'img': product.img['src'] if config.get('img') is None else get_image_url(product, config),
            'name': product.h2.text if config.get('name') is None else product.find(config['name']['tag'], class_=config['name']['class']).text,
            'link': website['base_url'] + product.find('a')['href'] if config.get('link') is None else website['base_url'] + product.find(config['link']['tag'], class_=config['link']['class'])['href']
        })
    if page is None:
        website['data'].append(data)
    else:
        page = data

    return data['clothes']

def get_image_url(product, config):
    try:
        product_image = product.find(config['img']['tag'], class_=config['img']['class']).img
        return product_image['src']
    except KeyError:
        return product_image['data-src']   

def get_html(url, current_page):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    return BeautifulSoup(requests.get(url + current_page, headers=headers).text, 'lxml')