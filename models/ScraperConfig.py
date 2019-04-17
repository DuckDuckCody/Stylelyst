from models.ScraperComponentText import ScraperComponentText
from models.ScraperComponentImage import ScraperComponentImage
from models.ScraperComponentLink import ScraperComponentLink
from models.ScraperComponentPrice import ScraperComponentPrice

class ScraperConfig():
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

    def get_components(self):
        return self.__components