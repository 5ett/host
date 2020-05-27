from datetime import datetime
from anime101 import app, cerberus, db
from flask import url_for, request, redirect, render_template, flash


@app.route('/')
def index():
    return render_template('index.html')
