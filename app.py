from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from formas import ContactForm
import smtplib

app = Flask(__name__)
app.config.from_object('config.Config')
app.config.from_object('config.DevConfig')

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


@app.route('/contact2', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print("success")
        return redirect(url_for("https://www.youtube.com/"))
    print("success2")
    return render_template('contact2.html', form=form)



@app.route('/cane')
def cane():
    return render_template('cane.html')


@app.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')


@app.route('/music_and_death')
def music_and_death():
    return render_template('music_and_death.html')


@app.route('/pedal')
def pedal():
    return render_template('pedal.html')


@app.route('/rudi')
def rudi():
    return render_template('rudi.html')


if __name__ == '__main__':
    app.run()
