from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': "Adam"}
    return render_template("index.html", title="Welcom page", user=user)
