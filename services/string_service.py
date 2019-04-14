import re

def price_string_to_float(price_string):
    return float(re.sub(r'[^0-9.]', '', price_string))