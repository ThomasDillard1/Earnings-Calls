//Fetch the api
//The api is not json, its is actually csv data
const api_key = process.env.API_KEY
const earnings_calendar = `https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=${API_KEY}`;

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
