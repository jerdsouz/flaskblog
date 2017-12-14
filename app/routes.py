from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Jerome'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in portland'
         },
        {
            'author': {'username': 'John'},
            'body': 'The avengers moview was so cool'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)
