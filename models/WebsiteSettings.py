from constants import WebsiteUrls as website_urls
from scraper_configs import *

# scraper_configs
# urls

WebsiteSettings = [
    # culture kings
    {
        'website_id': 2,
        'category': 1,
        'gender': 1,
        'base_url': website_urls.culture_kings,
        'url': website_urls.culture_kings + '/collections/mens-tops?page=',
        'scraper_config': culture_kings_config,
    },
    {
        'website_id': 2,
        'category': 2,
        'gender': 1,
        'base_url': website_urls.culture_kings,
        'url': website_urls.culture_kings + '/collections/mens-bottoms?page=',
        'scraper_config': culture_kings_config,
    },
    {
        'website_id': 2,
        'category': 1,
        'gender': 2,
        'base_url': website_urls.culture_kings,
        'url': website_urls.culture_kings + '/collections/womens-tops?page="',
        'scraper_config': culture_kings_config,
    },
    {
        'website_id': 2,
        'category': 2,
        'gender': 2,
        'base_url': website_urls.culture_kings,
        'url': website_urls.culture_kings + '/collections/womens-bottoms?page=',
        'scraper_config': culture_kings_config,
    },
    # the iconic
    {
        'website_id': 3,
        'category': 1,
        'gender': 1,
        'base_url': website_urls.the_iconic,
        'url': website_urls.the_iconic + '/mens-clothing-tshirts-singlets/?page=',
        'scraper_config': the_iconic_config,
    },
    {
        'website_id': 3,
        'category': 2,
        'gender': 1,
        'base_url': website_urls.the_iconic,
        'url': website_urls.the_iconic + '/mens-clothing-pants/?page=',
        'scraper_config': the_iconic_config,
    },
    {
        'website_id': 3,
        'category': 1,
        'gender': 2,
        'base_url': website_urls.the_iconic,
        'url': website_urls.the_iconic + '/womens-clothing-tops/?page=',
        'scraper_config': the_iconic_config,
    },
    {
        'website_id': 3,
        'category': 2,
        'gender': 2,
        'base_url': website_urls.the_iconic,
        'url': website_urls.the_iconic + '/womens-clothing-pants/?page=',
        'scraper_config': the_iconic_config,
    },
    # Peppermayo
    {
        'website_id': 4,
        'category': 1,
        'gender': 1,
        'base_url': website_urls.pepper_mayo,
        'url': website_urls.pepper_mayo + '/men/clothing/tops/shirts?p=',
        'scraper_config': pepper_mayo_config,
    },
    {
        'website_id': 4,
        'category': 2,
        'gender': 1,
        'base_url': website_urls.pepper_mayo,
        'url': website_urls.pepper_mayo + '/men/clothing/jeans-chino?p=',
        'scraper_config': pepper_mayo_config,
    },
    {
        'website_id': 4,
        'category': 1,
        'gender': 2,
        'base_url': website_urls.pepper_mayo,
        'url': website_urls.pepper_mayo + '/women/clothing/tops?p=',
        'scraper_config': pepper_mayo_config,
    },
    {
        'website_id': 4,
        'category': 2,
        'gender': 2,
        'base_url': website_urls.pepper_mayo,
        'url': website_urls.pepper_mayo + '/women/clothing/jeans?p=',
        'scraper_config': pepper_mayo_config,      
    }
]