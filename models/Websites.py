from services.scrapers import west_brother, culture_kings

west_brothers_url = "https://www.westbrothers.com.au"
culture_kings_url = "https://www.westbrothers.com.au"

Websites = [
    {
        'id': 1,
        'name': 'West Brothers',
        'clothes': [],
        'scrape_method': west_brother,
        'time_stamp': 0,
        'base_url': west_brothers_url,
        "urls": [
            {
                "id": 1,
                "gender": 1,
                "category": 1,
                "url": west_brothers_url
            }
        ]
    },
    {
        'id': 2,
        'name': 'Culture Kings',
        'clothes': [],
        'scrape_method': culture_kings,
        'time_stamp': 0,
        'url': culture_kings_url,
        "urls": [
            {
                "id": 1,
                "gender": 1,
                "category": 1,
                "url": culture_kings_url + "/collections/mens-tops?page="
            }
        ]
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