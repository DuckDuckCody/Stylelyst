from models.ScraperComponent import ScraperComponent

class ScraperComponentImage(ScraperComponent):
    def scrape(self, html_element):
        product_image = getattr(html_element.find(self.tag, class_=self._class), 'img', None)
        if product_image is not None:
            try:
                return product_image['src']
            except KeyError:
                return product_image['data-src']