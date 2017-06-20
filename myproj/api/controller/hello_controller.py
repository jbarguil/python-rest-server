"""Hello world controller.
"""

from myproj.api.model import HelloWorld


class HelloWorldController(object):
    """Hello world controller.
    """
    def __init__(self):
        super(HelloWorldController, self).__init__()

    def get_hello(self):
        """Returns a simple greeting object.
        """
        return HelloWorld()
