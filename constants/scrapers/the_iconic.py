from models.Scraper import Scraper
from constants.website_urls import website_urls

the_iconic = Scraper('figure', 'pinboard')
the_iconic.add_text_component('name', 'span', 'name')
the_iconic.add_price_component('price', 'span', 'price')
the_iconic.add_price_component('compare_price', 'span', 'old-price')
the_iconic.add_img_component('img', 'span', 'image-frame')
the_iconic.add_link_component('link', 'a', 'product-details', website_urls['the_iconic'])