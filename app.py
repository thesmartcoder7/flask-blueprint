from main import app
from main.public import public
from main import views
import config

# after blueprint creation in the main blueprint file,
# this next line registers it in the main
app.register_blueprint(public)



if __name__ == '__main__':
    app.run(debug=True)