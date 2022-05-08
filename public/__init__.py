from flask import Blueprint

# importing the blueprint class makes it possible to create an instance of a flask blueprint

public = Blueprint('public', __name__, static_folder='static', template_folder='templates', url_prefix='/public')

from . import views

# maintain the import steps to avoid circular imports
