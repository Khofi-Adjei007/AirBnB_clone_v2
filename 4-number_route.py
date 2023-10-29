mple Flask application
"""
from flask import Flask
"""
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

                                        @app.route('/python/', defaults={'text': 'is_cool'})
                                        @app.route('/python/<text>', strict_slashes=False)
                                        def display(text):
                                            """Display 'Python' followed by the value of the text parameter
                                                """
                                                    return "Python {}".format(text.replace("_", " "))

                                                    @app.route('/number/<int:n>', strict_slashes=False)
                                                    def num_display(n):
                                                        """Display '<n> is a number' where <n> is an integer
                                                            """
                                                                return "{} is a number".format(n)

                                                                if __name__ == "__main__":
                                                                    app.run()
