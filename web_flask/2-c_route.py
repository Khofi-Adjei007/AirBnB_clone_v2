#!/usr/bin/python3
from flask import Flask

# Create a Flask web application instance
app = Flask(__name)

# Define a route for the root URL ('/') that displays a greeting
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays a greeting message.
    
    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"

# Define a route for the '/hbnb' URL that displays 'HBNB'
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Displays the text 'HBNB'.
    
    Returns:
        str: The string 'HBNB'.
    """
    return "HBNB"

# Define a route for URLs like '/c/some_text' where 'some_text' can be any string
@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """
    Displays text based on the input.

    Args:
        text (str): The input text.
    
    Returns:
        str: The formatted text.
    """
    return 'C %s' % text.replace('_', ' ')

# Run the Flask application if this script is executed
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
