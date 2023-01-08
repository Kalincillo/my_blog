from flask import render_template, redirect, url_for
from . import main
from .forms import ContactForm


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/music')
def music():
    return render_template('music.html')


@main.route('/projects')
def projects():
    return render_template('projects.html')


@main.route('/hardware')
def hardware():
    return render_template('hardware.html')


@main.route('/software')
def software():
    return render_template('software.html')


@main.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("main.index"))
    return render_template('contact.html', form=form)


@main.route('/cane')
def cane():
    return render_template('cane.html')


@main.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')


@main.route('/music_and_death')
def music_and_death():
    return render_template('music_and_death.html')


@main.route('/pedal')
def pedal():
    return render_template('pedal.html')


@main.route('/rudi')
def rudi():
    return render_template('rudi.html')

@main.route('/burger')
def burger():
    return render_template('burger.html')


@main.route('/strength')
def strength():
    return render_template('strength.html')