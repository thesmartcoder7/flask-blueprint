from . import app
from .public import public
from . import views

app.register_blueprint(public)



if __name__ == '__main__':
    app.run(debug=True)