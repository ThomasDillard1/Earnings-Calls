from flask import Flask, jsonify, render_template
import requests
import json
from decouple import config

API_KEY = config('API_KEY')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# main driver function
if __name__ == '__main__':
    app.run()