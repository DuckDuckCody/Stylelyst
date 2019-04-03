from constants.WebsiteUrls import WebsiteUrls
from scraper_configs.ScraperConfigs import ScaperConfigs

WebsiteData = [
    # culture kings
    {
        'website_id': 2,
        'category': 1,
        'gender': 1,
        'expiry': 0,
        'base_url': WebsiteUrls.culture_kings.value,
        'url': WebsiteUrls.culture_kings.value + '/mens-tops?view=show-60&page=',
        'scraper_config': ScaperConfigs.culture_kings.value,
        'data': []
    },
    {
        'website_id': 2,
        'category': 2,
        'gender': 1,
        'expiry': 0,
        'base_url': WebsiteUrls.culture_kings.value,
        'url': WebsiteUrls.culture_kings.value + '/mens-bottoms?view=show-60&page=',
        'scraper_config': ScaperConfigs.culture_kings.value,
        'data': []
    },
    {
        'website_id': 2,
        'category': 1,
        'gender': 2,
        'expiry': 0,
        'base_url': WebsiteUrls.culture_kings.value,
        'url': WebsiteUrls.culture_kings.value + '/womens-tops?view=show-60&page="',
        'scraper_config': ScaperConfigs.culture_kings.value,
        'data': []
    },
    {
        'website_id': 2,
        'category': 2,
        'gender': 2,
        'expiry': 0,
        'base_url': WebsiteUrls.culture_kings.value,
        'url': WebsiteUrls.culture_kings.value + '/womens-bottoms?view=show-60&page=',
        'scraper_config': ScaperConfigs.culture_kings.value,
        'data': []
    },
    # the iconic
    {
        'website_id': 3,
        'category': 1,
        'gender': 1,
        'expiry': 0,
        'base_url': WebsiteUrls.the_iconic.value,
        'url': WebsiteUrls.the_iconic.value + '/mens-clothing-tshirts-singlets/?page=',
        'scraper_config': ScaperConfigs.the_iconic.value,
        'data': []
    },
    {
        'website_id': 3,
        'category': 2,
        'gender': 1,
        'expiry': 0,
        'base_url': WebsiteUrls.the_iconic.value,
        'url': WebsiteUrls.the_iconic.value + '/mens-clothing-pants/?page=',
        'scraper_config': ScaperConfigs.the_iconic.value,
        'data': []
    },
    {
        'website_id': 3,
        'category': 1,
        'gender': 2,
        'expiry': 0,
        'base_url': WebsiteUrls.the_iconic.value,
        'url': WebsiteUrls.the_iconic.value + '/womens-clothing-tops/?page=',
        'scraper_config': ScaperConfigs.the_iconic.value,
        'data': []
    },
    {
        'website_id': 3,
        'category': 2,
        'gender': 2,
        'expiry': 0,
        'base_url': WebsiteUrls.the_iconic.value,
        'url': WebsiteUrls.the_iconic.value + '/womens-clothing-pants/?page=',
        'scraper_config': ScaperConfigs.the_iconic.value,
        'data': []
    },
    # Peppermayo
    {
        'website_id': 4,
        'category': 1,
        'gender': 1,
        'expiry': 0,
        'base_url': WebsiteUrls.pepper_mayo.value,
        'url': WebsiteUrls.pepper_mayo.value + '/men/clothing/tops/shirts?p=',
        'scraper_config': ScaperConfigs.pepper_mayo.value,
        'data': []
    },
    {
        'website_id': 4,
        'category': 2,
        'gender': 1,
        'expiry': 0,
        'base_url': WebsiteUrls.pepper_mayo.value,
        'url': WebsiteUrls.pepper_mayo.value + '/men/clothing/jeans-chino?p=',
        'scraper_config': ScaperConfigs.pepper_mayo.value,
        'data': []
    },
    {
        'website_id': 4,
        'category': 1,
        'gender': 2,
        'expiry': 0,
        'base_url': WebsiteUrls.pepper_mayo.value,
        'url': WebsiteUrls.pepper_mayo.value + '/women/clothing/tops?p=',
        'scraper_config': ScaperConfigs.pepper_mayo.value,
        'data': []
    },
    {
        'website_id': 4,
        'category': 2,
        'gender': 2,
        'expiry': 0,
        'base_url': WebsiteUrls.pepper_mayo.value,
        'url': WebsiteUrls.pepper_mayo.value + '/women/clothing/jeans?p=',
        'scraper_config': ScaperConfigs.pepper_mayo.value,
        'data': []
    }
]



# lonley kids club
"""
{
    'website_id': 1,
    'category': 1,
    'gender': 1,
    'expiry': 0,
    'base_url': WEBSITE_URLS['LONLEY_KID'],
    'url': lonley_kids_club_url + 't-shirts/page/',
    'scraper_config': lonley_kids_club_config,
    'data': []
},
{
    'website_id': 1,
    'category': 2,
    'gender': 1,
    'expiry': 0,
    'base_url': lonley_kids_club_url,
    'url': lonley_kids_club_url + 'pants/page/',
    'scraper_config': lonley_kids_club_config,
    'data': []
},
{
    'website_id': 1,
    'category': 1,
    'gender': 2,
    'expiry': 0,
    'base_url': lonley_kids_club_url,
    'url': lonley_kids_club_url + 't-shirts/page/',
    'scraper_config': lonley_kids_club_config,
    'data': []
},
{
    'website_id': 1,
    'category': 2,
    'gender': 2,
    'expiry': 0,
    'base_url': lonley_kids_club_url,
    'url': lonley_kids_club_url + 'pants/page/',
    'scraper_config': lonley_kids_club_config,
    'data': []
},
"""