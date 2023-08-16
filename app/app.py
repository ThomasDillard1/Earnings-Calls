from flask import Flask, render_template, jsonify
from decouple import config

#Get the api key from the .env file
API_KEY = config('API_KEY')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# main driver function
if __name__ == '__main__':
    app.run(debug=True)