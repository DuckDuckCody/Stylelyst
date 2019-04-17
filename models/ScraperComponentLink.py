from models.ScraperComponent import ScraperComponent

class ScraperComponentLink(ScraperComponent):
    def __init__(self, name, tag, _class, base_url=None):
        super().__init__(name, tag, _class)
        self.base_url = base_url

    def scrape(self, html_element):
        url = html_element.find(self.tag, class_=self._class).get('href')
        if self.base_url:
            return self.base_url + url
        return url