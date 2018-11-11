###
# TODO
# track current page
# select category of clothes
# fiter the get clothes method with gender and categories
# move the get_clothe_html function to the scrapers end
###

# run script for windows
# ${env:FLASK_APP}='app.py'; ${env:FLASK_ENV}='development'; flask run

from models.Websites import Websites
from models.UserSettings import UserSettings
from models.Genders import Genders
from models.Categories import Categories
import flask
import time

app = flask.Flask(__name__)
user_settings = UserSettings()

@app.route("/")
def index():
    get_clothes()
    return flask.render_template('index.html', websites = Websites, user_settings = user_settings)

def get_clothes():
    for website in Websites:
        if website.get('id') in user_settings.websites and time.time() - website.get('time_stamp') > 86400: # 1 days
            website['clothes'] = website.get('scrape_method')(user_settings, website)
            website['time_stamp'] = time.time()

@app.route("/config", methods=['GET', 'POST'])
def config():
    if flask.request.method == 'POST':       
        user_settings.save_settings(flask.request.json)
        return flask.url_for('index')
    else:
        return flask.render_template('config.html', websites = Websites, genders = Genders, categories = Categories, user_settings = user_settings)
