from models.ScraperConfigText import ScraperConfigText
from models.ScraperConfigImage import ScraperConfigImage
from models.ScraperConfigLink import ScraperConfigLink
from models.ScraperConfigPrice import ScraperConfigPrice

class ScraperConfig():
    def __init__(self, container_tag, container_class):
        self.container_tag = container_tag
        self.container_class = container_class
        self.components = []

    def add_text_component(self, name, tag, _class):
        component = ScraperConfigText(name, tag, _class)
        self.__add_component(component)

    def add_img_component(self, name, tag, _class):
        component = ScraperConfigImage(name, tag, _class)
        self.__add_component(component)

    def add_link_component(self, name, tag, _class, url=None):
        component = ScraperConfigLink(name, tag, _class, url)
        self.__add_component(component)

    def add_price_component(self, name, tag, _class):
        component = ScraperConfigPrice(name, tag, _class)
        self.__add_component(component)

    def __add_component(self, component):
        self.components.append(component)