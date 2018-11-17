#find the javascript map equvialent to make this better
from bs4 import BeautifulSoup
import requests
import time

def scrape_website(user_settings, website):
    if website.get('id') == 1:
        west_brother(user_settings, website)
    elif website.get('id') == 2:
        culture_kings(user_settings, website)
    else:
        raise ValueError('Please set a scrape method for the website selected in scrapers.py')

def is_website_data_old(website_url_info):
    print(website_url_info)
    return (website_url_info.get('time_stamp') is not None and time.time() - website_url_info.get('time_stamp')) < 86400 # 1 days

def get_website_url_info(user_settings, website):
    return next((url for url in website.get('urls') if url['gender'] == user_settings.gender and url['category'] == user_settings.category), None)

def get_html(url):
    return BeautifulSoup(requests.get(url).text, 'lxml')

def west_brother(user_settings, website):

    website_url_info = get_website_url_info(user_settings, website)

    if is_website_data_old(website_url_info):
        for product in get_html(website_url_info.get('url')).find_all('div', class_="product-index"):
            website_url_info['clothes'].append({
                'price': product.span.text,
                'img': product.img['src'],
                'name': product.h3.text,
                'link': website.get('base_url') + product.find('div', class_="product-info").a['href']
            })

def culture_kings(user_settings, website):

    website_url_info = get_website_url_info(user_settings, website)

    if is_website_data_old(website_url_info):
        for product in get_html(website_url_info.get('url')).find_all('div', class_="product-grid-item"):
            website_url_info['clothes'].append({
                'price': product.find('span', class_="money").text,
                'img': product.find('div', class_="product-card__image").img['data-src'],
                'name': product.find('p', class_="product-title").a.text,
                'link': website.get('base_url') + product.find('a', class_="product-card__link")['href']
            })