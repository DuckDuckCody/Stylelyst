from models.Websites import Websites
from models.WebsiteData import WebsiteData
from models.UserSettings import UserSettings
from models.Genders import Genders
from models.Categories import Categories
from services.scraper import scrape_websites
from flask import Flask, render_template, redirect, flash, url_for, request

application = Flask(__name__)
user_settings = UserSettings()
website_data = WebsiteData

@application.route("/", methods=['GET'])
def index():
    current_page = request.args.get('page')
    if current_page is None:
        current_page = '1' 

    clothes = scrape_websites(user_settings, website_data, current_page)
    return render_template('index.html', clothes=clothes, current_page=current_page)

@application.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'POST':       
        user_settings.save_settings(request.json)
        return url_for('index')
    else:
        return render_template(
            'config.html', 
            websites=Websites, 
            genders=Genders, 
            categories=Categories, 
            user_settings=user_settings
        )