#find the javascript map equvialent to make this better
from bs4 import BeautifulSoup
import requests

def build_url(user_settings, website):
    urls = website.get('urls')

    print(next((url for url in urls if url.gender == user_settings.get('gender')), None))

def get_html(url):
    # 1 is current page
    return BeautifulSoup(requests.get(url + '1').text, 'lxml')

def west_brother(user_settings, website):
    clothes = []
    for product in get_html(website.get('base_url')).find_all('div', class_="product-index"):
        clothes.append({
            'price': product.span.text,
            'img': product.img['src'],
            'name': product.h3.text,
            'link': website.get('base_url') + product.find('div', class_="product-info").a['href']
        })
    return(clothes)

def culture_kings(user_settings, website):
    clothes = []
    for product in get_html(website.get('base_url')).find_all('div', class_="product-grid-item"):
        clothes.append({
            'price': product.find('span', class_="money").text,
            'img': product.find('div', class_="product-card__image").img['data-src'],
            'name': product.find('p', class_="product-title").a.text,
            'link': website.get('base_url') + product.find('a', class_="product-card__link")['href']
        })
    return(clothes)