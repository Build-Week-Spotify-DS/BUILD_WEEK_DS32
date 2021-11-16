from flask import Flask, render_template, request
from predict import pickle_model



APP = Flask(__name__)


@APP.route("/")
def index():
    """Base view."""
    return render_template('index.html', title="Spotify Song Suggester")
   


@ APP.route('/submit', methods=['GET'])
def submit(message=None):
    '''run throu a pickle model'''

    message = request.values['song']

    result = pickle_model(message)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    APP.run(debug=True)
