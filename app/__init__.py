from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_pymongo import PyMongo
# from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('app.configuration.DevelopmentConfig')

# Corriendo la lista de endpoints
from app import views
