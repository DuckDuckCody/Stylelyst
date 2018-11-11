#find the javascript map equvialent to make this better
from constants import west_brothers_url, culture_kings_url

def west_brother(html):
    clothes = []
    for product in html.find_all('div', class_="product-index"):
        clothes.append({
            'price': product.span.text,
            'img': product.img['src'],
            'name': product.h3.text,
            'link': west_brothers_url + product.find('div', class_="product-info").a['href']
        })
    return(clothes)

def culture_kings(html):
    clothes = []
    for product in html.find_all('div', class_="product-grid-item"):
        clothes.append({
            'price': product.find('span', class_="money").text,
            'img': product.find('div', class_="product-card__image").img['data-src'],
            'name': product.find('p', class_="product-title").a.text,
            'link': culture_kings_url + product.find('a', class_="product-card__link")['href']
        })
    return(clothes)