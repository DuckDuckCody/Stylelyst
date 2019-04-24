from flask import Flask, render_template, request, g
from constants import genders, categories, websites
from decorators.load_user_settings import load_user_settings
from services import scrape
from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()
application = Flask(__name__)

@application.route("/", methods=['GET'])
@load_user_settings
def index():
    page = request.args.get('page', '1')
    query_string = ''
    clothes = scrape(g.user_settings, query_string)
    return render_template('index.html', clothes=clothes, current_page=page)

@application.route("/search", methods=['GET'])
@load_user_settings
def search():
    query = request.args.get('query', '')
    query_string = ''
    clothes = scrape(g.user_settings, query_string)
    return render_template('index.html', clothes=clothes, current_page=None)

@application.route("/config", methods=['GET'])
@load_user_settings
def config():
    return render_template(
        'config.html', 
        websites=None, #websites=websites
        genders=genders, 
        categories=categories,
        user_settings=g.user_settings
    )