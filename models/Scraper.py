from models.ScraperComponentText import ScraperComponentText
from models.ScraperComponentImage import ScraperComponentImage
from models.ScraperComponentLink import ScraperComponentLink
from models.ScraperComponentPrice import ScraperComponentPrice
from services.html_service import get_html

class Scraper():
    def __init__(self, container_tag, container_class):
        self.container_tag = container_tag
        self.container_class = container_class
        self.__components = []

    def add_text_component(self, name, tag, _class):
        component = ScraperComponentText(name, tag, _class)
        self.__add_component(component)

    def add_img_component(self, name, tag, _class):
        component = ScraperComponentImage(name, tag, _class)
        self.__add_component(component)

    def add_link_component(self, name, tag, _class, base_url=None):
        component = ScraperComponentLink(name, tag, _class, base_url)
        self.__add_component(component)

    def add_price_component(self, name, tag, _class):
        component = ScraperComponentPrice(name, tag, _class)
        self.__add_component(component)

    def __add_component(self, component):
        self.__components.append(component)

    def scrape(self, url):
        page_html = get_html(url)
        html_elements = page_html.find_all(self.container_tag, class_=self.container_class)
        return [ self.__scrape_element(html_element) for html_element in html_elements ]

    def __scrape_element(self, html_element):
        return { component.name: component.scrape(html_element) for component in self.__components }