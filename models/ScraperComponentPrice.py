from models.ScraperComponent import ScraperComponent
from services.string_service import price_string_to_float

class ScraperComponentPrice(ScraperComponent):
    def scrape(self, html_element):
        price_text = getattr(html_element.find(self.tag, class_=self._class), 'text', '')
        return price_string_to_float(price_text)