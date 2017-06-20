"""Declares the API object.
"""

from flask import Blueprint

from myproj.api.routes.base_api import create_api


blueprint = Blueprint('hello_api_v1', __name__)
api = create_api(
    blueprint,
    version='1.0',
    title='Hello World API',
    description='API for greeting the big round world.',
)
