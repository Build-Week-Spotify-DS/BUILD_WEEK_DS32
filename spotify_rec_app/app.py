from flask import Flask, render_template, request
from predict import pickle_model
# from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)


@APP.route("/")
def index():
    """Base view."""
    return render_template('index.html', title="Spotify Song Suggester")
    # return f"HOME PAGE"


@ APP.route('/submit', methods=['GET'])
def submit(message=None):
    '''run throu a pickle model'''

    message = request.values['song']

    result = pickle_model(message)

    return render_template('index.html', result=result)


# APP.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# DB = SQLAlchemy(APP)
# class Record(DB.Model):
#     id = DB.Column(DB.Integer, primary_key=True)
#     datetime = DB.Column(DB.String(25))
#     # datetime = DB.Column(DB.DateTime)
#     value = DB.Column(DB.Float, nullable=False)
#     def __repr__(self):
#         return f"[id: {self.id},\
#                 datetime: {self.datetime},\
#                 value: {self.value}]"
if __name__ == "__main__":
    APP.run(debug=True)
