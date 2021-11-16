from flask import Flask, render_template, request
from .predict import pickle_model


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def index():
        """Base view."""
        return render_template('index.html', title="Spotify Song Suggester")

    @ app.route('/submit', methods=['GET', 'POST'])
    def submit(message=None):
        '''run array throu a pickle model'''

        message = request.values['song']

        result = pickle_model(message)

        return render_template('index.html', result=result)

    return app
