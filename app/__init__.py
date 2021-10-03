from flask import Flask
app = Flask(__name__)
app.config.from_object('app.configuration.DevelopmentConfig')
# Corriendo la lista de endpoints
from app.controllers import views
from app.controllers import login
from app.controllers import makereport
