from models.Scraper import Scraper
from constants.website_urls import website_urls

culture_kings = Scraper('div', 'product-grid-item')
culture_kings.add_text_component('name', 'p', 'product-title')
culture_kings.add_price_component('price', 'span', 'js-price')
culture_kings.add_price_component('compare_price', 'span', 'product-compare-price')
culture_kings.add_img_component('img', 'div', 'product-card__image')
culture_kings.add_link_component('link', 'a', 'product-card__link', website_urls['culture_kings'])