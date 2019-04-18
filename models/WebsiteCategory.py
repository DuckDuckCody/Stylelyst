from constants import websites
from services import list_service

class WebsiteCategory:
    def __init__(self, website_id, gender_id, category_id, url_extension):
        website = list_service.find_by_obj_attr(websites.websites, 'id', website_id)
        self.website_id = website.id
        self.name = website.name
        self.scraper = website.scraper
        self.base_url = website.base_url
        self.gender_id = gender_id
        self.category_id = category_id
        self.id = f"{self.website_id}{self.gender_id}{self.category_id}"
        self.url = f"{self.base_url}{url_extension}"

    def __str__(self):
        return "id: %s, name: %s, url: %s" % (self.id, self.name, self.url)