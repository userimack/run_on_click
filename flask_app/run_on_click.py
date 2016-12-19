#!/usr/bin/env python2

import flask

# Creating application
APP = flask.Flask(__name__)

"""
@APP.route('/')
def index():
    "Display the index page at '/'
    "
    return flask.render_template('index.html')
"""
@APP.route('/', methods=['POST', 'GET'])
def run():
    print ("I am running")
    return flask.render_template('index.html')

if __name__ == "__main__":
    APP.debug = True
    APP.run()
