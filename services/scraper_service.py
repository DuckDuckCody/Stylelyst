from constants.website_categories import website_categories

def scrape(user_settings, query_string):
    clothes = []
    for website_id in user_settings.website_ids:
        website_category = website_categories.get_category(website_id, user_settings.gender_id, user_settings.category_id)
        clothes = clothes + website_category.scrape()

    return clothes