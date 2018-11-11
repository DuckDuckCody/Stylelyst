###
# TODO
# track current page
# select category of clothes
# save settings to new user_settings model in config route
# move the get_clothe_html function to the scrapers end
###

from bs4 import BeautifulSoup
from models.websites import websites
from models.UserSettings import UserSettings
from models.genders import genders
from models.categories import categories
import flask
import requests
import time

app = flask.Flask(__name__)
user_settings = UserSettings()

@app.route("/")
def index():
    get_clothes()
    return flask.render_template('index.html', websites = websites, user_settings = user_settings)

def get_clothes():
    for website in websites:
        if website.get('id') in user_settings.websites and time.time() - website.get('time_stamp') > 86400: # 1 days
            website['clothes'] = website.get('scrape_method')(get_clothe_html((website.get('url'))))
            website['time_stamp'] = time.time()

def get_clothe_html(url):
    return BeautifulSoup(requests.get(url + str(user_settings.current_page)).text, 'lxml')

@app.route("/config", methods=['GET', 'POST'])
def config():
    if flask.request.method == 'POST':       
        user_settings.save_settings(flask.request.json)
        return flask.url_for('index')
    else:
        return flask.render_template('config.html', websites = websites, genders = genders, categories = categories, user_settings = user_settings)
