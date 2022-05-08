from flask import render_template
from . import app
from .public import public


app.register_blueprint(public)

# @app.route('/')
# def home():
#     return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)