from models.ScraperConfigComponent import ScraperConfigComponent

class ScraperConfigText(ScraperConfigComponent):
    def scrape(self, html_element):
        return getattr(html_element.find(self.tag, class_=self._class), 'text', '')