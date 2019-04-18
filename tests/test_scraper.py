import pytest
from application import application
from services import scrape_category_page
from constants import website_categories

@pytest.fixture
def client():
    application.config['TESTING'] = True
    return application.test_client()

# def test_each_website_category(client):
    # for website_category in website_categories:    
        # response = scrape_category_page(website_category.url + '1', website_category.scraper)
        # assert len(response) > 0