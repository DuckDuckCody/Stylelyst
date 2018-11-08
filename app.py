###
# TODO
# track current page
# select category of clothes
# way of only showing active websites in the websites view
# save settings to new user_settings model in config route
# make a base html file for every other template to inherit from
# <script src="{{ url_for('static', filename='bootstrap.min.js') }}"></script>
###

from bs4 import BeautifulSoup
from websites import websites
from models.user_settings import user_settings
from models.genders import genders
from models.categories import categories
import flask
import requests
import time

app = flask.Flask(__name__)
current_page = 1

@app.route("/")
def index():
    get_clothes()
    return flask.render_template('index.html', websites = websites)

def get_clothes():
    for website in websites:
        if website.get('id') in user_settings.get('websites') and time.time() - website.get('time_stamp') > 86400: # 1 days
            website['clothes'] = website.get('scrape_method')(get_clothe_html((website.get('url'))))
            website['time_stamp'] = time.time()

def get_clothe_html(url):
    return BeautifulSoup(requests.get(url + str(current_page)).text, 'lxml')

@app.route("/config", methods=['GET', 'POST'])
def config():
    if flask.request.method == 'POST':        
        save_settings(flask.request.form.to_dict())
        return flask.redirect(flask.url_for('index'))
    else:
        return flask.render_template('config.html', websites = websites, genders = genders, categories = categories, user_settings = user_settings)

def save_settings(settings):
    print(settings)
    for website in websites:
        if settings.get(str(website.get('id'))) == 'True':
            website['active'] = True
        else:
            website['active'] = False
