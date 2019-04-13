import pytest
from application import application
from services import scrape_website
from constants import website_categories

@pytest.fixture
def client():
    application.config['TESTING'] = True
    return application.test_client()

def test_each_website_category(client):
    for website_category in website_categories:    
        response = scrape_website(website_category, '1')
        assert len(response) > 0