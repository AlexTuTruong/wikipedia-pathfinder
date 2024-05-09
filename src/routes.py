import time

from flask import render_template, request, jsonify
from flask_socketio import SocketIO
from .utils.pathfinder import Pathfinder

from src import app
socketio = SocketIO(app)

display_path = True
pf = Pathfinder()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/find-path", methods=['POST'])
def find_path():
    if request.is_json:
        data = request.get_json()
        pf.get_shortest_path(data.get('startURL'), data.get('targetURL'), 6)
        return jsonify({'result': None}), 200
    else:
        return jsonify({'error': 'Request must contain JSON data'}), 400


@socketio.on('connect')
def handle_connect():
    global display_path
    display_path = True
    if display_path:
        socketio.start_background_task(get_path)


@socketio.on('disconnect')
def handle_disconnect():
    global display_path
    display_path = False


def get_path():
    global display_path
    while display_path:
        formatted_path = ' -> '.join(
            [link.removeprefix('https://en.wikipedia.org') for link in pf.path]
        )
        socketio.emit('number', formatted_path)
        time.sleep(0.25)
