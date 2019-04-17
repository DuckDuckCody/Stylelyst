from models.ScraperComponent import ScraperComponent

class ScraperComponentText(ScraperComponent):
    def scrape(self, html_element):
        return getattr(html_element.find(self.tag, class_=self._class), 'text', '')