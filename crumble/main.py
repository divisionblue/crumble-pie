from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
@app.route("/")
def hello():
    return "Hello World!"

def go():
    app.run()

if __name__ == "__main__":
    app.run()

