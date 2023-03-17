//Fetch the api
//The api is not json, its is actually csv data
const API_KEY = process.env.API_KEY;
const earnings_calendar = `https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=${API_KEY}`;

//Trying data with financial statements first
'use strict';
var request = require('request');

// replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
var url = `https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=${API_KEY}`;

var parsedData;
request.get({
    url: url,
    json: true,
    headers: {'User-Agent': 'request'}
  }, (err, res, data) => {
    if (err) {
      console.log('Error:', err);
    } else if (res.statusCode !== 200) {
      console.log('Status:', res.statusCode);
    } else {
      // data is successfully parsed as a JSON object:
      parsedData = JSON.parse(data);
      console.log(data);
    }
});

const container = document.getElementById('income-statement-container');

parsedData.forEach(item => {
  const div = document.createElement('div');
  div.innerHTML = `<p>${item.name}</p><p>${item.description}</p>`;
  container.appendChild(div);
});



//Earnings Call Data
/*
import scramjet from 'scramjet';
const { StringStream } = scramjet;
import r from 'request';
const { get } = r;

// replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
get(earnings_calendar)
    .pipe(new StringStream())
    .CSVParse()                                   // parse CSV output into row objects
    .each(object => console.log("Row:", object))
    .then(() => console.log("success"));
*/