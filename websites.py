import scrapers

west_brothers_url = "https://www.westbrothers.com.au"
culture_kings_url = "https://www.culturekings.com.au"

websites = [
    {
        'id': 1,
        'name': 'West Brothers',
        'url': 'https://www.westbrothers.com.au/collections/mens-clothing?page=',
        'clothes': [],
        'scrape_method': scrapers.west_brother,
        'time_stamp': 0
    },
    {
        'id': 2,
        'name': 'Culture Kings',
        'url': 'https://www.culturekings.com.au/collections/mens-tops?page=',
        'clothes': [],
        'scrape_method': scrapers.culture_kings,
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