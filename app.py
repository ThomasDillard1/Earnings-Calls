from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

