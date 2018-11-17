west_brothers_url = "https://www.westbrothers.com.au/"
culture_kings_url = "https://www.culturekings.com.au/collections/"

Websites = [
    {
        'id': 1,
        'name': 'West Brothers',
        'clothes': [],
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
        'base_url': culture_kings_url,
        "urls": [
            {
                "id": 1,
                "gender": 1,
                "category": 1,
                "url": culture_kings_url + "mens-tops?page=",
                "clothes": []
            },
            {
                "id": 2,
                "gender": 1,
                "category": 2,
                "url": culture_kings_url + "mens-bottoms?page=",
                "clothes": []
            },
            {
                "id": 3,
                "gender": 2,
                "category": 1,
                "url": culture_kings_url + "/womens-tops?page=",
                "clothes": []
            },
            {
                "id": 4,
                "gender": 2,
                "category": 2,
                "url": culture_kings_url + "/womens-bottoms?page=",
                "clothes": []
            }
        ]
    }
]