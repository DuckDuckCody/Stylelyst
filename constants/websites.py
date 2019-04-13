from constants.scraper_configs import *
from constants import website_urls
from models import Website

websites = [
    Website(1, 'Culture Kings', culture_kings_config, website_urls['culture_kings']),
    Website(2, 'The Iconic', the_iconic_config, website_urls['culture_kings']),
    Website(3, 'Peppermayo', pepper_mayo_config, website_urls['pepper_mayo'])
]