from flask import Blueprint

public = Blueprint('public', __name__, static_folder='static', template_folder='templates', url_prefix='/public')

from . import views
