from flask import render_template
from . import public

@public.route('/')
def home():
    return render_template('index.html')
    # return 'this is the public blueprint'