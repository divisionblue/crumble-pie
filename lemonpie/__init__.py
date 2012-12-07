from flask import Flask

lemonpie = Flask(__name__)
lemonpie.config.from_object('config')

from lemonpie import views
