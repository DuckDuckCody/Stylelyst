from models.ScraperConfigComponent import ScraperConfigComponent

class ScraperConfigLink(ScraperConfigComponent):
    def __init__(self, name, tag, _class, url):
        super().__init__(name, tag, _class)
        self.url = url

    def scrape(self, html_element):
        extension = html_element.find(self.tag, class_=self._class).get('href')
        if self.url:
            return self.url + extension
        return extension