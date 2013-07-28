import os
from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def hello():
    return redirect(url_for('static', filename='index.html'))