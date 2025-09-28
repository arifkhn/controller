from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/i')
def index_a():
    return render_template('index1.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('keyPress')
def handle_key_press(data):
    print('Received keyPress event:', data)
    emit('keyPress', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000)
