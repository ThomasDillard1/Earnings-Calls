from flask import Flask, render_template, request, redirect, url_for, session
from decouple import config
import requests

app = Flask(__name__)

#companies in the S&P 500 from scraping internet
companies = ['AAPL', 'MSFT', 'GOOG', 'GOOGL', 'AMZN', 'NVDA', 'BRK.B', 'META', 'TSLA', 'LLY', 'UNH', 'JNJ', 'V', 'JPM', 'WMT', 'XOM', 'MA', 'PG', 'AVGO', 'HD', 'ORCL', 'CVX', 'MRK', 'ABBV', 'KO', 'PEP', 'COST', 'ADBE', 'BAC', 'CSCO', 'MCD', 'ACN', 'TMO', 'CRM', 'PFE', 'CMCSA', 'DHR', 'LIN', 'NFLX', 'ABT', 'AMD', 'NKE', 'TMUS', 'DIS', 'WFC', 'TXN', 'UPS', 'PM', 'MS', 'AMGN', 'INTC', 'CAT', 'VZ', 'INTU', 'BA', 'COP', 'UNP', 'NEE', 'LOW', 'IBM', 'BMY', 'DE', 'RTX', 'HON', 'GE', 'SPGI', 'QCOM', 'AXP', 'AMAT', 'BKNG', 'SBUX', 'PLD', 'LMT', 'NOW', 'ELV', 'MDT', 'GS', 'SCHW', 'SYK', 'ISRG', 'ADP', 'TJX', 'T', 'BLK', 'MDLZ', 'GILD', 'MMC', 'CVS', 'ADI', 'VRTX', 'LRCX', 'REGN', 'ETN', 'ZTS', 'CI', 'C', 'AMT', 'CB', 'SLB', 'BDX', 'PGR', 'FISV', 'MO', 'BSX', 'EOG', 'SO', 'CME', 'HCA', 'ITW', 'ATVI', 'EQIX', 'DUK', 'MU', 'SHW', 'FDX', 'PYPL', 'SNPS', 'WM', 'KLAC', 'AON', 'NOC', 'MAR', 'CHTR', 'ICE', 'APD', 'CL', 'CDNS', 'HUM', 'MNST', 'GD', 'MCO', 'CSX', 'TGT', 'EL', 'MCK', 'ORLY', 'USB', 'MPC', 'ANET', 'FCX', 'MMM', 'OXY', 'EMR', 'PXD', 'ROP', 'PH', 'ECL', 'CMG', 'APH', 'NXPI', 'PSX', 'CTAS', 'PSA', 'PNC', 'AJG', 'STZ', 'EW', 'KDP', 'F', 'TDG', 'NSC', 'MSI', 'HES', 'RSG', 'TT', 'MET', 'VLO', 'FTNT', 'CARR', 'AZO', 'GM', 'HSY', 'AFL', 'ODFL', 'SRE', 'PCAR', 'PAYX', 'ADM', 'ADSK', 'MCHP', 'CCI', 'WELL', 'DXCM', 'KMB', 'GIS', 'WMB', 'NUE', 'MSCI', 'CPRT', 'AIG', 'DHI', 'IDXX', 'KHC', 'LVS', 'AEP', 'TEL', 'JCI', 'O', 'D', 'HLT', 'COF', 'ON', 'EXC', 'ROST', 'IQV', 'TFC', 'BIIB', 'KMI', 'TRV', 'SPG', 'MRNA', 'DOW', 'ABC', 'YUM', 'DLR', 'SYY', 'AME', 'DG', 'A', 'CTVA', 'GWW', 'BKR', 'HAL', 'LEN', 'OTIS', 'CTSH', 'CNC', 'LHX', 'BK', 'DD', 'AMP', 'VRSK', 'ROK', 'PRU', 'CEG', 'KR', 'FIS', 'CMI', 'BF.B', 'EA', 'FAST', 'PPG', 'XEL', 'WBD', 'GPN', 'DLTR', 'URI', 'LYB', 'DVN', 'HPQ', 'ED', 'NEM', 'VICI', 'PEG', 'VMC', 'WST', 'OKE', 'PWR', 'ALL', 'MLM', 'FTV', 'DAL', 'ALGN', 'AWK', 'GLW', 'APTV', 'CDW', 'IR', 'RMD', 'KEYS', 'ILMN', 'WEC', 'EIX', 'IT', 'FANG', 'MTD', 'RCL', 'ANSS', 'AVB', 'CBRE', 'ZBH', 'NDAQ', 'TROW', 'WBA', 'EQR', 'XYL', 'TSCO', 'SBAC', 'TTWO', 'EFX', 'WY', 'MPWR', 'MKC', 'CHD', 'CAH', 'EBAY', 'ULTA', 'DFS', 'ES', 'STE', 'HIG', 'HPE', 'GPC', 'STT', 'HRL', 'RJF', 'DTE', 'BAX', 'BR', 'ALB', 'MTB', 'K', 'VRSN', 'AEE', 'CTRA', 'FE', 'WTW', 'BRO', 'ROL', 'ETR', 'ARE', 'HWM', 'NVR', 'WAB', 'JBHT', 'LYV', 'LUV', 'GRMN', 'FLT', 'DOV', 'CLX', 'DRI', 'LH', 'TSN', 'TDY', 'PPL', 'PFG', 'COO', 'MOH', 'RF', 'CCL', 'PHM', 'ENPH', 'HOLX', 'CNP', 'PAYC', 'FITB', 'IRM', 'EXR', 'ATO', 'BALL', 'PTC', 'BBY', 'J', 'FOXA', 'VTR', 'EXPD', 'WAT', 'SWKS', 'UAL', 'MAA', 'IEX', 'CINF', 'HBAN', 'CMS', 'FDS', 'IFF', 'WRB', 'NTAP', 'FOX', 'TYL', 'NTRS', 'OMC', 'MRO', 'TER', 'AKAM', 'EXPE', 'MGM', 'ESS', 'TXT', 'DGX', 'CF', 'SJM', 'INCY', 'CAG', 'AVY', 'POOL', 'SNA', 'LKQ', 'L', 'SWK', 'EPAM', 'AMCR', 'LW', 'SYF', 'DPZ', 'ZBRA', 'TAP', 'NDSN', 'VTRS', 'TRMB', 'KMX', 'APA', 'LDOS', 'STX', 'CFG', 'PKG', 'BEN', 'EVRG', 'MAS', 'MOS', 'CE', 'TECH', 'WDC', 'CPB', 'LNT', 'UDR', 'IPG', 'MTCH', 'NWS', 'AES', 'NWSA', 'KIM', 'IP', 'NLOK', 'CZR', 'HST', 'JKHY', 'CPT', 'PNR', 'BIO', 'CDAY', 'PEAK', 'CHRW', 'FMC', 'NI', 'WYNN', 'GL', 'REG', 'AOS', 'TFX', 'CRL', 'AAL', 'BXP', 'HSIC', 'KEY', 'PARA', 'EMN', 'BWA', 'DVA', 'QRVO', 'ALLE', 'MKTX', 'FFIV', 'SEDG', 'UHS', 'ETSY', 'HAS', 'HII', 'PNW', 'JNPR', 'BBWI', 'NRG', 'WRK', 'CTLT', 'XRAY', 'TPR', 'FRT', 'VFC', 'RHI', 'RL', 'AIZ', 'WHR', 'NCLH', 'IVZ', 'GNRC', 'CMA', 'MHK', 'OGN', 'ALK', 'ZION', 'PVH', 'SEE', 'LNC', 'NWL', 'DXC', 'AAP', 'VNO', 'DISH', 'PENN', 'LUMN', 'EMBC']

#Get the api key from the .env file
API_KEY = config('API_KEY')
API_BASE_URL = 'https://www.alphavantage.co'

#Secret key for sessions in Flask
SECRET_KEY = config('SECRET_KEY')
app.secret_key = SECRET_KEY


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        company_ticker = request.form['ticker'] #comes from the name of the <input> in index.html
        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={company_ticker}&apikey={API_KEY}'
        r = requests.get(url)
        data = r.json()
        session[company_ticker] = data
        return redirect(url_for("company_overview", ticker=company_ticker))
    else:
        return render_template('index.html', companies=companies)


#Next step is to create an html page for this rendering and then style it I guess
@app.route('/<ticker>', methods=['POST', 'GET'])
def company_overview(ticker):
    if ticker in session:
        company_data = session[ticker]
        return render_template('company.html', ticker=ticker, company_data=company_data)
    else:
        #if ticker doesn't exist, then make them enter a new ticker
        return redirect(url_for(index))

if __name__ == '__main__':
    app.run(debug=True)