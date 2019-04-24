from models.WebsiteCategory import WebsiteCategory

class WebsiteCategories():
    def __init__(self):
        self.__categories = {}

    def add_category(self, website, gender_id, category_id, url_extension):
        website_category = WebsiteCategory(website, url_extension)
        key = f"{website.id}{gender_id}{category_id}"
        self.__categories[key] = website_category

    def get_category(self, website_id, gender_id, category_id):
        key = f"{website_id}{gender_id}{category_id}"
        return self.__categories[key]