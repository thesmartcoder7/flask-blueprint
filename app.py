from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is the home page'


@app.route('/about')
def about():
    return 'this is the about page'

if __name__ == '__main__':
    app.run(debug=True)