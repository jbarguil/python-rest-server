"""main.py

Main file of our API.
"""

import flask
import re

from werkzeug.contrib.fixers import ProxyFix

from config import config
from myproj.api.routes.hello_v1 import blueprint as hello_api_v1


# Creates Flask app.
app = flask.Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = config.SESSION_SECRET
app.debug = config.DEBUG

# Registers supported API versions.
app.register_blueprint(hello_api_v1, url_prefix='/api/hello/v1')


if config.DEBUG:
    # Creates Swagger documentation page.
    @app.route('/')
    def docs_home():
        return flask.render_template('docs-home.html', api_flavors=[
            # TODO: Add your APIs (manually, sorry).
            {
                'name': 'Hello World API',
                'url_prefix': '/api/hello/v1',
            },
        ])


# --------------------------------------------------------------------------- #
#                   CROSS-ORIGIN RESOURCE SHARING (CORS)                      #
# --------------------------------------------------------------------------- #

_ROOT = 'https?://.*\.?'    # HTTP or HTTPS + optional subdomain.
_ALLOWED_CORS_DOMAINS = [
    _ROOT + 'example\.com',
]

if config.DEBUG:
    _ALLOWED_CORS_DOMAINS += [
        _ROOT + 'localhost',
        _ROOT + '127\.0\.0\.1',
    ]

# Compiles allowed domains into regular expression objects for verification.
_ALLOWED_CORS_DOMAINS = map(re.compile, _ALLOWED_CORS_DOMAINS)


@app.after_request
def after_request(response):
    """Adds headers to allow Cross-Origin Resource Sharing (CORS).

    This allows webpages from other domains to access us.
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
    """
    def is_origin_allowed(origin):
        for regex in _ALLOWED_CORS_DOMAINS:
            if re.match(regex, origin) is not None:
                return True
        return False

    origin = flask.request.environ.get('HTTP_ORIGIN', '')
    if is_origin_allowed(origin):
        response.headers.add('Access-Control-Allow-Origin', origin)
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, Accept')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PUT, DELETE, OPTIONS')
        # response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


if __name__ == '__main__':
    from myproj.scripts.base import print_env_alert
    print_env_alert()

    if app.debug:
        app.run(host='0.0.0.0', threaded=True)
    else:
        app.run()
