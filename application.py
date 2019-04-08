from flask import Flask, render_template, request, g
from models import Websites, WebsiteSettings, Genders, Categories
from services import scrape_websites
from decorators import load_user_settings
from werkzeug.contrib.cache import SimpleCache

application = Flask(__name__)
cache = SimpleCache()

@application.route("/", methods=['GET'])
@load_user_settings
def index():
    current_page = request.args.get('page')
    if current_page is None:
        current_page = '1'

    clothes = scrape_websites(g.user_settings, WebsiteSettings, current_page, cache)
    return render_template('index.html', clothes=clothes, current_page=current_page)

@application.route("/config", methods=['GET'])
@load_user_settings
def config():
    return render_template(
        'config.html', 
        websites=Websites, 
        genders=Genders, 
        categories=Categories, 
        user_settings=g.user_settings
    )