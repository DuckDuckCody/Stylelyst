###
# TODO
# track current page
# make a nice looking frontend with bulma
###

from models.Websites import Websites
from models.UserSettings import UserSettings
from models.Genders import Genders
from models.Categories import Categories
from services.scraper import scrape_websites
import flask

app = flask.Flask(__name__)
user_settings = UserSettings()

@app.route("/", methods=['GET'])
def index():
    user_settings.current_page = flask.request.args.get('page')
    hot_clothes = scrape_websites(user_settings, Websites)
    return flask.render_template('index.html', hot_clothes = hot_clothes, user_settings = user_settings)

@app.route("/config", methods=['GET', 'POST'])
def config():
    if flask.request.method == 'POST':       
        user_settings.save_settings(flask.request.json)
        return flask.url_for('index')
    else:
        return flask.render_template('config.html', websites = Websites, genders = Genders, categories = Categories, user_settings = user_settings)
