from app import app
from datetime import date

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
