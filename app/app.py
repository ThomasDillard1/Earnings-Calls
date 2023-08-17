from flask import Flask, render_template, request
from decouple import config
import requests

#Get the api key from the .env file
API_KEY = config('API_KEY')
API_BASE_URL = 'https://www.alphavantage.co'
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    companies = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'META', 'GOOG', 'TSLA', 'BRK.B', 'UNH', 'JNJ', 'JPM', 'XOM', 'LLY', 'V', 'PG', 'AVGO', 'HD', 'MA', 'CVX', 'MRK', 'ABBV', 'PEP', 'COST', 'ADBE', 'KO', 'WMT', 'CSCO', 'MCD', 'BAC', 'TMO', 'CRM', 'PFE']
    return render_template('index.html', companies=companies)
    # if request.method == 'POST':
    #    company = request.form['company_']


if __name__ == '__main__':
    app.run(debug=True)