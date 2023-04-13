# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required
from config import Config
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin

# App
app = Flask(__name__)
# app.config.from_object(Config)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app)

ma = Marshmallow(app)
jwt = JWTManager(app)

# Database
db = SQLAlchemy()

# Item model


class Item(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

# Routes


@app.route('/')
# @cross_origin
def index():
    return render_template('index.html')


# Socket IO
# Initialize server_first_start variable as True
server_first_start = True


@socketio.on('connect')
def handle_connect():
    global server_first_start
    if server_first_start:
        # Send message to reload page for first start
        emit('message', {'data': 'reload page for first start'})
        server_first_start = False
    else:
        emit('message', {'data': 'Hello'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


# Run server
if __name__ == '__main__':
    socketio.run(app)
