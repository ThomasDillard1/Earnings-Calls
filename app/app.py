from flask import Flask, render_template, request, redirect, url_for, session
from decouple import config
import requests

app = Flask(__name__)
#companies in the S&P 500
companies = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'META', 'GOOG', 'TSLA', 'BRK.B', 'UNH', 'JNJ', 'JPM', 'XOM', 'LLY', 'V', 'PG', 'AVGO', 'HD', 'MA', 'CVX', 'MRK', 'ABBV', 'PEP', 'COST', 'ADBE', 'KO', 'WMT', 'CSCO', 'MCD', 'BAC', 'TMO', 'CRM', 'PFE']

#Get the api key from the .env file
API_KEY = config('API_KEY')
API_BASE_URL = 'https://www.alphavantage.co'
SECRET_KEY = config('SECRET_KEY')
app.secret_key = SECRET_KEY


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        company_ticker = request.form['ticker'] #comes from the name of the <input> in index.html
        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={company_ticker}&apikey={API_KEY}'
        r = requests.get(url)
        data = r.json()
        print(data)
        session[company_ticker] = data
        return redirect(url_for("company_overview", ticker=company_ticker))
    else:
        return render_template('index.html', companies=companies)


@app.route('/<ticker>', methods=['POST', 'GET'])
def company_overview(ticker):
    if ticker in session:
        company_data = session[ticker]
        return f"<h2>{ticker}</h2><br>{company_data}"
    else:
        return redirect(url_for(index))

if __name__ == '__main__':
    app.run(debug=True)