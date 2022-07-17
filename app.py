from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DATABASE_URI'] = 'sqlite://///home/ivan/Projects/website/blog.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
