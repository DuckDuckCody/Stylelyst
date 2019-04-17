from services import list_service, get_html

def scrape_websites(user_settings, website_settings, current_page, cache):
    all_clothes = []
    for website in user_settings.websites:
        cache_key = f"{website}{user_settings.gender}{user_settings.category}{current_page}"
        clothes = cache.get(cache_key)
        if clothes is None:
            clothes = []
            current_website_settings = list_service.find_by_obj_attr(website_settings, 'id', cache_key[:-1])  
            if current_website_settings:  
                clothes = scrape_website(current_website_settings.url + current_page, current_website_settings.scraper_config)
                cache.set(cache_key, clothes, timeout=86400)

        all_clothes = all_clothes + clothes

    return all_clothes

def scrape_website(url, config):
    page_html = get_html(url)
    html_elements = page_html.find_all(config.container_tag, class_=config.container_class)
    return [ scrape_element(html_element, config.get_components()) for html_element in html_elements ]

def scrape_element(html_element, components):
    return { component.name: component.scrape(html_element) for component in components }