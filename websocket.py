from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

viewer_count = 0

@app.route("/join")
def join_stream():
    global viewer_count

    viewer_count += 1

    socketio.emit(
        "viewer_update",
        {"viewers": viewer_count}
    )

    return {"message": "Viewer joined"}

if __name__ == "__main__":
    socketio.run(app)
