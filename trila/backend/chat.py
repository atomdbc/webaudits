from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

from app import create_app, socketio

app = create_app(debug=True)
CORS(app)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000)




