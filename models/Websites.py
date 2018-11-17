lonley_kids_club_url = "https://lonelykidsclub.com/"
culture_kings_url = "https://www.culturekings.com.au/collections/"

Websites = [
    {
        'id': 1,
        'name': 'Lonley Kids Club',
        'clothes': [],
        'base_url': lonley_kids_club_url,
        'scraper_config': {
            'container': {
                'tag': 'li',
                'class': 'product'
            },
            'price': None,
            'img': None,
            'name': None,
            'link': None
        },
        "urls": [
            {
                "gender": 1,
                "category": 1,
                "url": lonley_kids_club_url + "t-shirts/page/1",
                "clothes": []
            },
            {
                "gender": 1,
                "category": 2,
                "url": lonley_kids_club_url + "pants/page/1",
                "clothes": []
            },
            {
                "gender": 2,
                "category": 1,
                "url": lonley_kids_club_url + "t-shirts/page/1",
                "clothes": []
            },
            {
                "gender": 2,
                "category": 2,
                "url": lonley_kids_club_url + "pants/page/1",
                "clothes": []
            }
        ]
    },
    {
        'id': 2,
        'name': 'Culture Kings',
        'clothes': [],
        'base_url': culture_kings_url,
        'scraper_config': {
            'container': {
                'tag': 'div',
                'class': 'product-grid-item'
            },
            'price': {
                'tag': 'span',
                'class': 'money'
            },
            'img': {
                'tag': 'div',
                'class': 'product-card__image'
            },
            'name': {
                'tag': 'p',
                'class': 'product-title'
            },
            'link': {
                'tag': 'a',
                'class': 'product-card__link'
            }
        },
        "urls": [
            {
                "gender": 1,
                "category": 1,
                "url": culture_kings_url + "mens-tops?page=",
                "clothes": []
            },
            {
                "gender": 1,
                "category": 2,
                "url": culture_kings_url + "mens-bottoms?page=",
                "clothes": []
            },
            {
                "gender": 2,
                "category": 1,
                "url": culture_kings_url + "/womens-tops?page=",
                "clothes": []
            },
            {
                "gender": 2,
                "category": 2,
                "url": culture_kings_url + "/womens-bottoms?page=",
                "clothes": []
            }
        ]
    }
]