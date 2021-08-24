from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
## todaviano hemos iterado el secret
app.config['SECRET_KEY'] = 'secret!'
## debemos limitar la conexion del cors con solo el link de origen de la app de produccion
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
## Renderiza el landing page
def index(): return render_template('index.html')

@socketio.on('FtoBMsj')
def handleFtoBCmd(json):
    print('Message: ',str(json))
    
@socketio.on('FtoBCmd')
def handleFtoBCmd(json):
    print(str(json))
    send(json, broadcast = True)
## leer en flask soketio como enviar por broadcast a todas las paginas con el mensaje correspondienmte

if __name__ == '__main__':
    socketio.run(app)