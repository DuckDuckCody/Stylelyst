from services import list_service, get_html, string_service

def scrape_websites(user_settings, website_settings, current_page, cache):
    all_clothes = []
    for website in user_settings.websites:
        cache_key = f"{website}{user_settings.gender}{user_settings.category}{current_page}"
        clothes = cache.get(cache_key)
        if clothes is None:
            clothes = []
            current_website_settings = list_service.find_by_obj_attr(website_settings, 'id', cache_key[:-1])  
            if current_website_settings:  
                clothes = scrape_website(current_website_settings, current_page)
                cache.set(cache_key, clothes, timeout=86400)

        all_clothes = all_clothes + clothes

    return all_clothes

def scrape_website(website_settings, current_page):
    clothes = [] 
    config = website_settings.scraper_config
    page_html = get_html(website_settings.url, current_page)
    for product in page_html.find_all(config['container']['tag'], class_=config['container']['class']):
        clothes.append({
            'price': get_product_price(product, config),
            'compare_price': get_product_compare_price(product, config),
            'img': get_product_image_url(product, config),
            'name': getattr(product.find(config['name']['tag'], class_=config['name']['class']), 'text', 'N/A'),
            'link': website_settings.base_url + product.find(config['link']['tag'], class_=config['link']['class']).get('href')
        })
        
    return clothes

def get_product_price(product, config):
    product_price_container = getattr(product.find(config['price']['tag'], class_=config['price']['class']), 'text', '')
    product_price = product_price_container.split(' ')[-1]
    return string_service.price_string_to_float(product_price)

def get_product_compare_price(product, config):
    compare_price = getattr(product.find(config['compare_price']['tag'], class_=config['compare_price']['class']), 'text', '')
    if compare_price is not '':
        return string_service.price_string_to_float(compare_price)
    return compare_price

def get_product_image_url(product, config):
    product_image = getattr(product.find(config['img']['tag'], class_=config['img']['class']), 'img', None)
    if product_image is not None:
        try:
            return product_image['src']
        except KeyError:
            return product_image['data-src']