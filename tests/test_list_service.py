import pytest
from application import application
from models import Website
from services import list_service

@pytest.fixture
def test_list():
    return [
        Website('1', 'first website', '', ''),
        Website('2', 'second website', '', '')
    ]

def test_find_obj(test_list):
    res = list_service.find_by_obj_attr(test_list, 'id', '1')
    assert res.name == 'first website'

def test_handle_invalid_key(test_list):
    res = list_service.find_by_obj_attr(test_list, 'ider', '1')
    assert res == None

def test_handle_invalid_value(test_list):
    res = list_service.find_by_obj_attr(test_list, 'id', '3')
    assert res == None

def test_handle_empty_list():
    res = list_service.find_by_obj_attr([], 'id', '1')
    assert res == None

def test_handle_invalid_list_type():
    res = list_service.find_by_obj_attr('id', 'id', '1')
    assert res == None