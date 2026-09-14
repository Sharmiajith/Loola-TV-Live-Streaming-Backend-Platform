
from flask import Blueprint
from flask import Flask

stream_bp = Blueprint('stream', __name__)

app = Flask(__name__)

app.register_blueprint(stream_bp)

@app.route("/")
def home():
    return "Loola Backend Running"

if __name__ == "__main__":
    app.run(debug=True)