#find the javascript map equvialent to make this better
from bs4 import BeautifulSoup
import requests
import time

def scrape_websites(user_settings, websites):
    for website in websites:
        if website.get('id') in user_settings.websites:
            scrape_website(user_settings, website)

def scrape_website(user_settings, website):
    website_url_info = get_website_url_info(user_settings, website)
    if website_url_info.get('time_stamp') is None or time.time() - website_url_info.get('time_stamp') > 86400: # if clothes data over 1 day old
        if website.get('id') == 1:
            lonley_kids_club(website_url_info)
        elif website.get('id') == 2:
            culture_kings(website_url_info)
        else:
            print("website id not found scrapers.scrape_method")

def get_website_url_info(user_settings, website):
    return next((url for url in website.get('urls') if url['gender'] == user_settings.gender and url['category'] == user_settings.category), None)

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    return BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')

# find a way to refactor these methods
def lonley_kids_club(url_info):
    url_info['clothes'] = []
    for product in get_html(url_info.get('url')).find_all('li', class_="product"):
        url_info['clothes'].append({
            'price': product.span.text,
            'img': product.img['src'],
            'name': product.h2.text,
            'link': "https://lonelykidsclub.com/" + product.find('a')['href']
        })
    url_info['time_stamp'] = time.time()

def culture_kings(url_info):
    url_info['clothes'] = []
    for product in get_html(url_info.get('url')).find_all('div', class_="product-grid-item"):
        url_info['clothes'].append({
            'price': product.find('span', class_="money").text,
            'img': product.find('div', class_="product-card__image").img['data-src'],
            'name': product.find('p', class_="product-title").a.text,
            'link': "https://www.culturekings.com.au/" + product.find('a', class_="product-card__link")['href']
        })
    url_info['time_stamp'] = time.time()