from models.Website import Website
from constants.scrapers import culture_kings
from constants.website_urls import website_urls

culture_kings = Website('1', 'Culture Kings', culture_kings, website_urls.get('culture_kings'))