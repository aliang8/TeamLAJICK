#import flask
from flask import Flask, render_template, session, redirect, url_for
from utils import functions
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = '1'


@app.route()
def dashboard():
    return

@app.route()
def login():
    return

@app.route()
def logout():
    return

@app.route()
def profile():
    return

if __name__ == "__main__":
    app.debug = True
    app.run()
