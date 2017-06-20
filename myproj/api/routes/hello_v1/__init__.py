"""v1 of the Hello API
"""

from .api import api, blueprint

from .hello import namespace as ns_hello


api.add_namespace(ns_hello)
