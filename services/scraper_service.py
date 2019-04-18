from services import list_service

def scrape_category(user_settings, website_categories, current_page, cache):
    setting_id_extension = f"{user_settings.gender}{user_settings.category}"
    return scrape(user_settings.websites, website_categories, setting_id_extension, cache)

def scrape_search(user_settings, website_categories, query, cache):
    cache_extension = f"{query}-query"
    return scrape(user_settings.websites, website_categories, cache_extension, cache)

def scrape(websites, website_categories, setting_id_extension, cache):
    all_items = []
    for website in websites:
        website_setting = list_service.find_by_obj_attr(website_categories, 'id', website + setting_id_extension)  
        cache_key = website_setting + current_page
        items = cache.get(cache_key)
        if items is None:
            # website_setting = list_service.find_by_obj_attr(website_categories, 'id', cache_key[:-1])  
            # url = website_setting.url + current_page
            url = websites_settings.url
            items = website_settings.scraper.scrape(url)
            cache.set(cache_key, items, timeout=86400)

        all_items = all_items + items

    return all_items