from services import price_string_to_float

def test_price_string_to_float():
    res = price_string_to_float('\n !!? ?dwafe f sa  f sd$509.78 \n \n')
    assert res == 509.78