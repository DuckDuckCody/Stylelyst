from models.WebsiteCategories import WebsiteCategories
from constants.websites import *

website_categories = WebsiteCategories()
# culture kings
website_categories.add_category(culture_kings, 1, 1, '/collections/mens-top')
website_categories.add_category(culture_kings, 1, 2, '/collections/mens-top-jacket')
website_categories.add_category(culture_kings, 1, 3, '/collections/mens-bottoms')
website_categories.add_category(culture_kings, 1, 4, '/collections/markdowns/gender-mens')
website_categories.add_category(culture_kings, 2, 1, '/collections/womens-tops')
website_categories.add_category(culture_kings, 2, 2, '/collections/womens-tops-jacket')
website_categories.add_category(culture_kings, 2, 3, '/collections/womens-bottoms')
website_categories.add_category(culture_kings, 2, 4, '/collections/markdowns/gender-womens')
# the iconic
website_categories.add_category(the_iconic, 1, 1, '/mens-clothing-tshirts-singlets')
website_categories.add_category(the_iconic, 1, 2, '/mens-clothing-coats-jackets')
website_categories.add_category(the_iconic, 1, 3, '/mens-clothing-pants')
website_categories.add_category(the_iconic, 1, 4, '/mens-clothing-sale')
website_categories.add_category(the_iconic, 2, 1, '/womens-clothing-tops')
website_categories.add_category(the_iconic, 2, 2, '/womens-clothing-coats-jackets')
website_categories.add_category(the_iconic, 2, 3, '/womens-clothing-pants')
website_categories.add_category(the_iconic, 2, 4, '/womens-clothing-sale')
# peppermayo
website_categories.add_category(pepper_mayo, 1, 1, '/men/clothing/tops/shirts')
website_categories.add_category(pepper_mayo, 1, 3, '/men/clothing/jeans-chino')
website_categories.add_category(pepper_mayo, 1, 4, '/men/sale')
website_categories.add_category(pepper_mayo, 2, 1, '/women/clothing/tops')
website_categories.add_category(pepper_mayo, 2, 3, '/women/clothing/jeans')
website_categories.add_category(pepper_mayo, 2, 4, '/women/sale')