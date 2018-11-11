west_brothers_url = "https://www.westbrothers.com.au"
culture_kings_url = "https://www.culturekings.com.au"

# run script for windows
# ${env:FLASK_APP}='app.py'; ${env:FLASK_ENV}='development'; flask run

website_urls = [
    {
        "website_id": 2,
        "base_url": culture_kings_url,
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