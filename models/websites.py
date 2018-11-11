from services.scrapers import west_brother, culture_kings
from constants import west_brothers_url, culture_kings_url

Websites = [
    {
        'id': 1,
        'name': 'West Brothers',
        'url': west_brothers_url + '/collections/mens-clothing?page=',
        'clothes': [],
        'scrape_method': west_brother,
        'time_stamp': 0
    },
    {
        'id': 2,
        'name': 'Culture Kings',
        'url': culture_kings_url + '/collections/mens-tops?page=',
        'clothes': [],
        'scrape_method': culture_kings,
        'time_stamp': 0
    }
]

#clothes =  [
#    {
#        "gender": 1,
#        "category": 4,
#        "items": [
#            {
#                "price": 0,
#                "name": "dwa",
#                "img": "dwa"
#            }
#        ]
#    }
#]