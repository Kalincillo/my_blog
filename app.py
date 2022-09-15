from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DEBUG MODE
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

app.config['DATABASE_URI'] = 'sqlite://///home/ivan/Projects/website/blog.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')



@app.route('/hardware')
def hardware():
    return render_template('hardware.html')


@app.route('/software')
def software():
    return render_template('software.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cane')
def cane():
    return render_template('cane.html')



if __name__ == '__main__':
    app.run(debug=True)
