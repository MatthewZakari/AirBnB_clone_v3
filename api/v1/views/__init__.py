from flask import Blueprint

app_views = Blueprint('api_veiws', __name__, url_prefix='/api/v1')

# Wildcard import is ignored by linters, don't worry about warning
from api.v1.views.index import *
