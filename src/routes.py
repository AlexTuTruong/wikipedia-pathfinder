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

        current_formatted_path = []
        for link in pf.path:
            strippedlink = link.removeprefix('https://en.wikipedia.org')
            current_formatted_path.append(
                f'<a href="{link}" target="_blank" class="hover:underline">{strippedlink}</a>'
            )

        cleaned_currrent_path = ' -> '.join(link for link in current_formatted_path)
        socketio.emit('paths', cleaned_currrent_path)

        unformatted_paths = pf.solutions.copy()
        sols = ''
        for paths in unformatted_paths:
            formatted_path = []
            for url in paths:
                strippedurl = url.removeprefix('https://en.wikipedia.org')
                formatted_path.append(f'<a href="{url}" target="_blank" class="hover:underline">{strippedurl}</a>')

            cleaned_path = ' -> '.join(path for path in formatted_path)
            sols += f'<li>{cleaned_path}</li>'

        socketio.emit('solutions', sols)
        time.sleep(0.35)
