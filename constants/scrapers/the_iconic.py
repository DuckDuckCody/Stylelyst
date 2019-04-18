from models import Scraper
from constants.website_urls import website_urls

the_iconic_config = Scraper('figure', 'pinboard')
the_iconic_config.add_text_component('name', 'span', 'name')
the_iconic_config.add_price_component('price', 'span', 'price')
the_iconic_config.add_price_component('compare_price', 'span', 'old-price')
the_iconic_config.add_img_component('img', 'span', 'image-frame')
the_iconic_config.add_link_component('link', 'a', 'product-details', website_urls['the_iconic'])