from flask import Blueprint

public = Blueprint('public', __name__,  static_folder='static/public_static', template_folder='templates/public_templates')

from . import views
