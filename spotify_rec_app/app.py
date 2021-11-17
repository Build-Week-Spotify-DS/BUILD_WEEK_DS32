from flask import Flask, render_template, request
# from .predict import pickle_model
from .getting_stuff_from_spotify import get_song_params


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

        s_chacteristic, s_params = get_song_params(message)

        return render_template('song_params.html', s_chacteristic=s_chacteristic, s_params=s_params)

    return app
