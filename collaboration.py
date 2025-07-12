from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

document_content = ""

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('load', document_content)

@socketio.on('update')
def handle_update(data):
    global document_content
    document_content = data
    emit('update', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)

