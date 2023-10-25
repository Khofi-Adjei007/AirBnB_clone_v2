#!/usr/bin/python3
from flask import Flask

# Create a Flask web application instance
app = Flask(__name)

# Define a route for the root URL ('/') that displays a greeting


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display a greeting message.

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"

# Define a route for the '/hbnb' URL that displays 'HBNB'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Display 'HBNB'.

    Returns:
        str: The string 'HBNB'.
    """
    return "HBNB"


# Run the Flask application if this script is executed

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
