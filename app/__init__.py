from flask import Flask
from flask_socketio import SocketIO, send
app = Flask(__name__)

app.config.from_object('app.configuration.DevelopmentConfig')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

# Corriendo la lista de endpoints
from app.controllers import views
from app.controllers import login
from app.controllers import makereport

