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
        pf.solutions = []
        pf.get_shortest_path(data.get('startURL'), data.get('targetURL'), 6)
        return jsonify({'result': None}), 200
    else:
        return jsonify({'error': 'Request must contain JSON data'}), 400


@socketio.on('connect')
def handle_connect():
    global display_path
    display_path = True
    if display_path:
        socketio.start_background_task(get_paths)


@socketio.on('disconnect')
def handle_disconnect():
    global display_path
    display_path = False


def get_paths():
    global display_path
    while display_path:
        formatted_path = ' -> '.join(
            [link.removeprefix('https://en.wikipedia.org') for link in pf.path]
        )
        socketio.emit('paths', formatted_path)

        unformatted_paths = pf.solutions.copy()
        sols = ''
        for paths in unformatted_paths:
            cleaned_path = ' -> '.join(path.removeprefix('https://en.wikipedia.org') for path in paths)
            sols += f'<li>{cleaned_path}</li>'

        socketio.emit('solutions', sols)
        time.sleep(0.25)
