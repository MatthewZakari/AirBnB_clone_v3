from flask import Blueprint

app_views = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Wildcard import is ignored by linters, don't worry about warning
from . import index  # Assuming index.py in same folder
