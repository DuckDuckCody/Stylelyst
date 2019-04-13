import pytest
from application import application

@pytest.fixture
def client():
    application.config['TESTING'] = True
    return application.test_client()

def test_config_page(client):
    res = client.get('/config')
    assert 200 == res.status_code

def test_index_page(client):
    res = client.get('/')
    assert 200 == res.status_code
    
def test_index_multiple_websites(client):
    client.set_cookie('/', 'gender', '1') 
    client.set_cookie('/', 'category', '1')
    client.set_cookie('/', 'websites', '1,2,3')
    res = client.get('/')
    assert b'culturekings' in res.data
    assert b'theiconic' in res.data
    assert b'peppermayo' in res.data

def test_index_single_website(client):
    client.set_cookie('/', 'gender', '1') 
    client.set_cookie('/', 'category', '1')
    client.set_cookie('/', 'websites', '1')
    res = client.get('/')
    assert b'culturekings' in res.data
    assert b'theiconic' not in res.data