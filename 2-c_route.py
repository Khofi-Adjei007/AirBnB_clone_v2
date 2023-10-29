#!/usr/bin/python3
"""Simple Flask application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
        """Display a greeting message
            """
                return "Hello HBNB!"

            @app.route("/hbnb", strict_slashes=False)
            def HBNB():
                    """Display 'HBNB'
                        """
                            return "HBNB"

                        @app.route('/c/<text>', strict_slashes=False)
                        def text(text):
                                """Display the text provided in the URL
                                    """
                                        return "C {}".format(text.replace("_", " "))

                                    if __name__ == "__main__":
                                            app.run()
