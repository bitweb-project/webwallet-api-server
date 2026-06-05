# app.py
from gevent import monkey
monkey.patch_all()

import sys
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"), override=True)

sys.path.insert(0, os.path.dirname(__file__))

from server import app, socketio

if __name__ == "__main__":
    socketio.run(
        app,
        host  = os.environ.get("HOST", "0.0.0.0"),
        port  = int(os.environ.get("PORT", "21223")),
        debug = os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes"),
    )
