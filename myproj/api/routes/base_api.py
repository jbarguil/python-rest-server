"""Declares the API object and Exception handling.
"""

from flask_restplus import Api

from config import config


def create_api(blueprint, version, title, description):
    """Creates a new API object.
    """
    api = Api(
        blueprint,
        version=version,
        title=title,
        description=description,
        doc='/' if config.DEBUG else False,
    )

    @api.errorhandler(KeyError)
    def handle_error_ke(e):
        """Raised when a KeyError is raised."""
        return {
           'message': "Mandatory parameter '{}' missing".format(e.message)
        }, 400

    @api.errorhandler(ValueError)
    def handle_error_ve(e):
        """Raised when a ValueError is raised."""
        return {'message': '{}'.format(e.message)}, 400

    return api
