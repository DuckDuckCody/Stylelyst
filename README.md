# Python Clothes
A python app that scrapes online Australian clothing stores for products and puts them all on this one website.

run script for windows
${env:FLASK_APP}='application.py'; ${env:FLASK_ENV}='development'; flask run

run script for linux
export FLASK_ENV=development
export FLASK_APP=application.py
flask run