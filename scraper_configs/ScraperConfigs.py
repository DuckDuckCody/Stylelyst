from enum import Enum
from scraper_configs.culture_kings import culture_kings_config
from scraper_configs.the_iconic import the_iconic_config
from scraper_configs.pepper_mayo import pepper_mayo_config

class ScaperConfigs(Enum): 
    culture_kings = culture_kings_config
    the_iconic = the_iconic_config
    pepper_mayo = pepper_mayo_config