from models.Websites import Websites
from models.WebsiteData import WebsiteData
from models.Genders import Genders
from models.Categories import Categories
from services.scraper import scrape_websites
from decorators.load_user_settings import load_user_settings
from flask import Flask, render_template, redirect, flash, url_for, request

application = Flask(__name__)
website_data = WebsiteData

@application.route("/", methods=['GET'])
@load_user_settings
def index():
    current_page = request.args.get('page')
    if current_page is None:
        current_page = '1' 

    clothes = scrape_websites(request.user_settings, website_data, current_page)
    return render_template('index.html', clothes=clothes, current_page=current_page)

@application.route("/config", methods=['GET'])
@load_user_settings
def config():
    return render_template(
        'config.html', 
        websites=Websites, 
        genders=Genders, 
        categories=Categories, 
        user_settings=request.user_settings
    )