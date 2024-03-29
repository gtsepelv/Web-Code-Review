from flask import Flask, render_template
from main import *

app = Flask(__name__)


@app.route("/")
def index():
    data = collection.find()
    return render_template("index.html", data=data)


get_data()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
