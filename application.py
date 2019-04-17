from flask import Flask, render_template, request, g
from constants import website_categories, websites, genders, categories
from services import scrape_websites
from decorators import load_user_settings
from werkzeug.contrib.cache import SimpleCache

# TODO
# improve config naming scheme and parameters **DONE**
# improve scrape_websites
# add search route logic

application = Flask(__name__)
cache = SimpleCache()

@application.route("/", methods=['GET'])
@load_user_settings
def index():
    current_page = request.args.get('page', '1')
    clothes = scrape_websites(g.user_settings, website_categories, current_page, cache)
    return render_template('index.html', clothes=clothes, current_page=current_page)

@application.route("/search", methods=['GET'])
@load_user_settings
def search():
    query = request.args.get('query')
    return "Search Page!: " + query

@application.route("/config", methods=['GET'])
@load_user_settings
def config():
    return render_template(
        'config.html', 
        websites=websites,
        genders=genders, 
        categories=categories, 
        user_settings=g.user_settings
    )