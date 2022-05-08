from flask import render_template
from . import public # this gets the blueprint into the views


@public.route('/')
def home():
    return render_template('public/index.html')
    

@public.route('/about')
def about():
    return render_template('public/about.html')
    