"""Warm greeting endpoints.
"""

import flask

from flask_restplus import Namespace, Resource

from myproj.api.controller import HelloWorldController

from .api import api
from .views import register_json_filters


namespace = Namespace('hello',
                      path='/hello',
                      description='Hello world greetings')
register_json_filters(namespace)


hello_controller = HelloWorldController()


@namespace.route('')
class HelloWorld(Resource):
    """Show a nice warm greeting."""

    @namespace.doc('get_hello')
    @namespace.marshal_with(namespace.models['HelloWorld'])
    def get(self):
        """Show a nice warm greeting."""
        return hello_controller.get_hello()
