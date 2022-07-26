
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return '<h1 style= "text-align: center;color: red" >"Hello", World!"</h1>'\
           '<img src="https://media.giphy.com/media/l0HlPZgHWCuJiPtSg/giphy.gif" >'


@app.route("/<name>")
def bye(name):
    return f"bye hi {name}"




if __name__ == "__main__":
    app.run(debug =True)
