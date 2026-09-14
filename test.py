from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

socketio.run(app)
from flask import Flask


@app.route("/")
def home():
    return "Loola TV Backend Running"

app.run(debug=True)