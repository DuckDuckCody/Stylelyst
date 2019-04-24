class WebsiteCategory:
    def __init__(self, website, url_extension):
        self.website_id = website.id
        self.name = website.name
        self.scraper = website.scraper
        self.base_url = website.base_url
        self.url = f"{self.base_url}{url_extension}"

    def scrape(self):
        return self.scraper.scrape(self.url)

    def __str__(self):
        return "name: %s, url: %s" % (self.name, self.url)