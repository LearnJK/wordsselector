from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def index(): return render_template('index.html')

@socketio.on('message')
def handleMessage(m):
    print('Message: ',m)
    send(m, broadcast = True)

@socketio.on('m')
def handleM(m):
    print('M: ',m)
    send(m, broadcast = True)

@socketio.on('FtoBCmd')
def handle_my_custom_event(json):
    print(str(json))

if __name__ == '__main__':
    socketio.run(app)