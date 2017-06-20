"""Defines the structure of JSONs returned to clients, based on model classes.
"""

from flask_restplus import Model, fields


_models = {}


def register_json_filters(api):
    for name, model in _models.items():
        api.models[name] = model


_models['HelloWorld'] = Model('HelloWorld', {
    'message': fields.String(
        description='Hello message'),
})
