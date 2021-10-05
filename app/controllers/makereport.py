from flask import url_for, redirect, render_template, flash, g, session, request
from flask_socketio import send
from app import socketio

from app.models import makereport

@socketio.on('FToPMsj')
def handleFtoBCmd(json):
    print('Message: ',str(json))
    
@socketio.on('FToPCmd')
def handleFtoBCmd(json):
    print(str(json))
    # send(json, broadcast = True)

