from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def index(): return render_template('index.html')

@socketio.on('FtoBMsj')
def handleFtoBCmd(json):
    print('Message: ',str(json))
    
@socketio.on('FtoBCmd')
def handleFtoBCmd(json):
    print(str(json))
    send(json, broadcast = True)
#leer en flask soketio como enviar por broadcast a todas las paginas con el mensaje correspondienmte

if __name__ == '__main__':
    socketio.run(app)

# @socketio.on('m')
# def handleM(m):
#     print('M: ',m)
#     send(m, broadcast = True)