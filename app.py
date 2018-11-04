###
# Todo
# 
###

from bs4 import BeautifulSoup
from websites import websites
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
        if website.get('active') and time.time() - website.get('time_stamp') > 86400: # 1 days
            website['clothes'] = scrape_website(website.get('scrape_method'), (website.get('url')))
            website['time_stamp'] = time.time()

def scrape_website(scrape_method, url):
    return scrape_method(get_clothe_html(url))

def get_clothe_html(url):
    return BeautifulSoup(requests.get(url + str(current_page)).text, 'lxml')

@app.route("/config", methods=['GET', 'POST'])
def config():
    if flask.request.method == 'POST':        
        save_settings(flask.request.form.to_dict())
        return flask.redirect(flask.url_for('index'))
    else:
        return flask.render_template('config.html', websites = websites)

def save_settings(settings):
    for website in websites:
        if settings.get(str(website.get('id'))) == 'True':
            website['active'] = True
        else:
            website['active'] = False