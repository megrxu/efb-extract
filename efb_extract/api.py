from flask import Flask, jsonify
from .load import get_users, get_chats, get_raws, get_self

app = Flask(__name__)


@app.route("/")
@app.route("/users/")
def users():
    return jsonify(get_users())


@app.route("/chats/")
def chats():
    return jsonify(get_chats())


@app.route("/self/")
def show_self():
    return jsonify(get_self())


@app.route("/raws/")
def raws():
    return jsonify(get_raws())
