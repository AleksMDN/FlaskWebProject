"""
Routes and views for the flask application.
"""
from vsearch import search4letters
from datetime import datetime
from flask import render_template, request
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/results', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           title='Here are your results:',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           year=datetime.now().year
     )

@app.route('/entry')
def entry():
    """Renders the home page."""
    return render_template(
        'entry.html',
        title='Welcome to search4letters on the web!',
        year=datetime.now().year
    )