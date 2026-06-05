import logging
import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-me-in-production")
app.url_map.strict_slashes = False
CORS(app)

socketio = SocketIO(app, async_mode="gevent", cors_allowed_origins="*")


@app.route("/")
def index():
    return render_template("index.html")


from server import rest  # noqa: E402
rest.init(app)
