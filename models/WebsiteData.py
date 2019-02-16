from constants import lonley_kids_club_url, culture_kings_url
from scraper_configs.culture_kings import culture_kings_config
from scraper_configs.lonley_kids_club import lonley_kids_club_config

WebsiteData = [
    # lonley kids club
    {
        'website_id': 1,
        'category': 1,
        'gender': 1,
        'expiry': 0,
        'base_url': lonley_kids_club_url,
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
    # culture kings
    {
        'website_id': 2,
        'category': 1,
        'gender': 1,
        'expiry': 0,
        'base_url': culture_kings_url,
        'url': culture_kings_url + 'mens-tops?view=show-60&page=',
        'scraper_config': culture_kings_config,
        'data': []
    },
    {
        'website_id': 2,
        'category': 2,
        'gender': 1,
        'expiry': 0,
        'base_url': culture_kings_url,
        'url': culture_kings_url + 'mens-bottoms?view=show-60&page=',
        'scraper_config': culture_kings_config,
        'data': []
    },
    {
        'website_id': 2,
        'category': 1,
        'gender': 2,
        'expiry': 0,
        'base_url': culture_kings_url,
        'url': culture_kings_url + 'womens-tops?view=show-60&page="',
        'scraper_config': culture_kings_config,
        'data': []
    },
    {
        'website_id': 2,
        'category': 2,
        'gender': 2,
        'expiry': 0,
        'base_url': culture_kings_url,
        'url': culture_kings_url + 'womens-bottoms?view=show-60&page=',
        'scraper_config': culture_kings_config,
        'data': []
    }
]