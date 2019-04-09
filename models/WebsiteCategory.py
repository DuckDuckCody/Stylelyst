from models.Websites import Websites
from services.ListManager import ListManager

class WebsiteCategory:
    def __init__(self, website_id, gender, category, url_extension):
        lm = ListManager()
        website = lm.find_by_obj_attr(Websites, 'id', website_id)
        self.website_id = website.id
        self.name = website.name
        self.scraper_config = website.scraper_config
        self.base_url = website.base_url
        self.gender = gender
        self.category = category
        self.id = f"{self.website_id}{self.gender}{self.category}"
        self.url = f"{self.base_url}{url_extension}"