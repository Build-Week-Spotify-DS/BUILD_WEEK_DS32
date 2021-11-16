from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)


@APP.route("/")
def index():
    """Base view."""
    return render_template('index.html')
    # return f"HOME PAGE"

@APP.route('/submit')
def submit():
    '''run throu a pickle model'''
    return f'RECOMMENDING...'



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
