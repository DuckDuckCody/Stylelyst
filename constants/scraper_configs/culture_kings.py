from models import ScraperConfig
from constants.website_urls import website_urls

culture_kings_config = ScraperConfig('div', 'product-grid-item')
culture_kings_config.add_text_component('name', 'p', 'product-title')
culture_kings_config.add_price_component('price', 'span', 'js-price')
culture_kings_config.add_price_component('compare_price', 'span', 'product-compare-price')
culture_kings_config.add_img_component('img', 'div', 'product-card__image')
culture_kings_config.add_link_component('link', 'a', 'product-card__link', website_urls['culture_kings'])