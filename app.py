from flask import Flask
from flask import render_template
from flask import url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware


from website import app as flask_app_1
from weather import app as flask_app_2
application = DispatcherMiddleware(flask_app_1, {
    '/weather': flask_app_2
})