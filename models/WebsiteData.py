from constants import WebsiteUrls as website_urls
from scraper_configs import *

WebsiteData = [
    # culture kings
    {
        'website_id': 2,
        'category': 1,
        'gender': 1,
        'expiry': 0,
        'base_url': website_urls.culture_kings,
        'url': website_urls.culture_kings + '/mens-tops?view=show-60&page=',
        'scraper_config': culture_kings_config,
        'data': []
    },
    {
        'website_id': 2,
        'category': 2,
        'gender': 1,
        'expiry': 0,
        'base_url': website_urls.culture_kings,
        'url': website_urls.culture_kings + '/mens-bottoms?view=show-60&page=',
        'scraper_config': culture_kings_config,
        'data': []
    },
    {
        'website_id': 2,
        'category': 1,
        'gender': 2,
        'expiry': 0,
        'base_url': website_urls.culture_kings,
        'url': website_urls.culture_kings + '/womens-tops?view=show-60&page="',
        'scraper_config': culture_kings_config,
        'data': []
    },
    {
        'website_id': 2,
        'category': 2,
        'gender': 2,
        'expiry': 0,
        'base_url': website_urls.culture_kings,
        'url': website_urls.culture_kings + '/womens-bottoms?view=show-60&page=',
        'scraper_config': culture_kings_config,
        'data': []
    },
    # the iconic
    {
        'website_id': 3,
        'category': 1,
        'gender': 1,
        'expiry': 0,
        'base_url': website_urls.the_iconic,
        'url': website_urls.the_iconic + '/mens-clothing-tshirts-singlets/?page=',
        'scraper_config': the_iconic_config,
        'data': []
    },
    {
        'website_id': 3,
        'category': 2,
        'gender': 1,
        'expiry': 0,
        'base_url': website_urls.the_iconic,
        'url': website_urls.the_iconic + '/mens-clothing-pants/?page=',
        'scraper_config': the_iconic_config,
        'data': []
    },
    {
        'website_id': 3,
        'category': 1,
        'gender': 2,
        'expiry': 0,
        'base_url': website_urls.the_iconic,
        'url': website_urls.the_iconic + '/womens-clothing-tops/?page=',
        'scraper_config': the_iconic_config,
        'data': []
    },
    {
        'website_id': 3,
        'category': 2,
        'gender': 2,
        'expiry': 0,
        'base_url': website_urls.the_iconic,
        'url': website_urls.the_iconic + '/womens-clothing-pants/?page=',
        'scraper_config': the_iconic_config,
        'data': []
    },
    # Peppermayo
    {
        'website_id': 4,
        'category': 1,
        'gender': 1,
        'expiry': 0,
        'base_url': website_urls.pepper_mayo,
        'url': website_urls.pepper_mayo + '/men/clothing/tops/shirts?p=',
        'scraper_config': pepper_mayo_config,
        'data': []
    },
    {
        'website_id': 4,
        'category': 2,
        'gender': 1,
        'expiry': 0,
        'base_url': website_urls.pepper_mayo,
        'url': website_urls.pepper_mayo + '/men/clothing/jeans-chino?p=',
        'scraper_config': pepper_mayo_config,
        'data': []
    },
    {
        'website_id': 4,
        'category': 1,
        'gender': 2,
        'expiry': 0,
        'base_url': website_urls.pepper_mayo,
        'url': website_urls.pepper_mayo + '/women/clothing/tops?p=',
        'scraper_config': pepper_mayo_config,
        'data': []
    },
    {
        'website_id': 4,
        'category': 2,
        'gender': 2,
        'expiry': 0,
        'base_url': website_urls.pepper_mayo,
        'url': website_urls.pepper_mayo + '/women/clothing/jeans?p=',
        'scraper_config': pepper_mayo_config,
        'data': []
    }
]