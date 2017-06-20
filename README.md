# MyProj Python REST API #

REST API for accessing MyProj's engine.
Version 0.1.

## General info ##

* Production environment: <TODO: add URL>
* Dev environment: <TODO: add URL>
* Client documentation automatically generated using Swagger, available at root web page of the DEV API.

### How do I get set up? ###

* Install Python 2.7.
* From root directory, run `pip install -r requirements.txt`.

It is highly recommended that you do this from within a virtual environment!

If you have any problems, contact the team and we'll update these instructions!

### Running local dev server ###

* Set your environment variables (listed in `config.py`) in your local copy of the `.env` file. These vars include access keys for the database and other services. You should ask for them beforehand.
* From root directory, run `python main.py`.
    * *Tip*: if for some reason you don't see your code changes reflect in the server's behavior, try running `cleanpyc.sh` and restarting it.

It is also possible to use the classes in Python shell for testing. For this, we highly recommend using [IPython](https://ipython.org/) instead of Python's vanilla shell, as it has more features, such as auto-complete. Example (from root directory):

```python
In [1]: import myproj.api.model as m

In [2]: hello = m.HelloWorld()

In [3]: print(hello.message)
Hello, world!
```

## Code organization ##

The code follows the Model-View-Controller (MVC) pattern. Main packages:

* `myproj.api.model`: main model classes.
* `myproj.api.controller`: main controller classes.
* `myproj.api.routes`: views, in this case, you may understand it as "REST interfaces".
    * Each submodule contains their own `views` submodule, which defines the JSON objects that are returned to clients, as well as related Swagger documentation.


### Scripts ###

The `scripts` module contains any scripts that were useful at some point for experimenting, developing and testing.
Hopefully by the time you are reading this, the useful ones have already been integrated into the codebase and are accessible via REST APIs.

### External links ###

We are using the following libraries and services:

* Python libraries:
    * [Flask](http://flask.pocoo.org/): for dealing with the web.
    * [Flask Restplus](https://flask-restplus.readthedocs.io/en/stable/): for easier REST interface.
    * [Python DotEnv](https://pypi.python.org/pypi/python-dotenv): for managing environment variables.

### Who do I talk to? ###

* Dev team via email or homing pigeons.
* <TODO: Add your contacts>
