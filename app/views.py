from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': "Adam"}
    posts = [
        {'author': {"nickname":"John"},
         'body': 'What a beautifull life'
         },
        {'author':{'nickname':'Peter'},
         'body': 'War and Piece'
         }
    ]
    return render_template("index.html", title='Welcom page', user=user, posts=posts)
