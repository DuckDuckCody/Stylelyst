from models.Scraper import Scraper

pepper_mayo = Scraper('li', 'item product product-item')
pepper_mayo.add_text_component('name', 'p', 'product-item-name')
pepper_mayo.add_price_component('price', 'span', 'current-price')
pepper_mayo.add_price_component('compare_price', 'span', 'original-price')
pepper_mayo.add_img_component('img', 'a', 'product photo product-item-photo')
pepper_mayo.add_link_component('link', 'a', 'product-item-link')