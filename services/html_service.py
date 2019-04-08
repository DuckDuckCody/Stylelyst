import requests
from bs4 import BeautifulSoup

def get_html(url, current_page):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    url = f"{url}{current_page}"
    page_text = requests.get(url, headers=headers).text
    return BeautifulSoup(page_text, 'lxml')