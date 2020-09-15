"""
Routes and views for the flask application.
"""
from vsearch import search4letters
from datetime import datetime
from flask import render_template
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

@app.route('/search4')
def search4() -> str:
    """Renders the results of a call to 'search4letters' to the browser."""
    return render_template(
       'search4.html',
       title='Result4Search',
       year=datetime.now().year,
       message=str(search4letters('life, the universe, and everything', 'xyz'))
       )