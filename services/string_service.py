import re

def price_string_to_float(price_string):
    clean_price_string = re.sub(r'[^0-9.]', '', price_string).strip()
    if clean_price_string == '':
        return clean_price_string
    return float(clean_price_string)