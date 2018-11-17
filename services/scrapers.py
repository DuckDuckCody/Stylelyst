#find the javascript map equvialent to make this better
from bs4 import BeautifulSoup
import requests
import time

def scrape_websites(user_settings, websites):
    for website in websites:
        if website.get('id') in user_settings.websites:
            find_website(user_settings, website)

def find_website(user_settings, website):
    website_url_info = get_website_url_info(user_settings, website)
    if website_url_info.get('time_stamp') is None or time.time() - website_url_info.get('time_stamp') > 86400: # if clothes data over 1 day old
        scrape_wesbite(website.get('base_url'), website.get('scraper_config'), website_url_info)

def get_website_url_info(user_settings, website):
    return next((url for url in website.get('urls') if url['gender'] == user_settings.gender and url['category'] == user_settings.category), None)

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    return BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')

def scrape_wesbite(base_url, config, url_info):
    
    url_info['clothes'] = []
    for product in get_html(url_info.get('url')).find_all(config['container']['tag'], class_=config['container']['class']):
        url_info['clothes'].append({
            'price': product.span.text if config.get('price') is None else product.find(config['price']['tag'], class_=config['price']['class']).text,
            'img': product.img['src'] if config.get('img') is None else product.find(config['img']['tag'], class_=config['img']['class']).img['data-src'],
            'name': product.h2.text if config.get('name') is None else product.find(config['name']['tag'], class_=config['name']['class']).a.text,
            'link': base_url + product.find('a')['href'] if config.get('link') is None else base_url + product.find(config['link']['tag'], class_=config['link']['class'])['href']
        })
    url_info['time_stamp'] = time.time()