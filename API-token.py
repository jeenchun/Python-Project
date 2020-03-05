# FROM: https://www.worldtradingdata.com/members/home

# Your API Token: UFrhoimO1z70qsISJolfEH8cQFHrPsPe7LJ04ZvnwDjdgCVQ7s13Wc5KnvMU

# EXAMPLE REQUEST

import requests
import json

url = 'https://api.worldtradingdata.com/api/v1/stock'
params = {
  'symbol': 'SNAP,TWTR,VOD.L',
  'api_token': 'UFrhoimO1z70qsISJolfEH8cQFHrPsPe7LJ04ZvnwDjdgCVQ7s13Wc5KnvMU'
}
response = requests.request('GET', url, params=params)
response.json()

# EXAMLE RESPONSE: STOCKS AND INDICES

{
    "total_returned": 5,
    "total_results": 5,
    "total_pages": 1,
    "limit": 50,
    "page": 1,
    "data": [
        {
            "symbol": "SNAP",
            "name": "Snap Inc.",
            "currency": "USD",
            "price": "13.85",
            "stock_exchange_long": "New York Stock Exchange",
            "stock_exchange_short": "NYSE"
        },
        ...
    ]
}
  
# FOR DAX PERFORMANCE INDEX:
# Your API Links
# Real time

https://api.worldtradingdata.com/api/v1/stock?symbol=^DAX&api_token=UFrhoimO1z70qsISJolfEH8cQFHrPsPe7LJ04ZvnwDjdgCVQ7s13Wc5KnvMU

# History

https://api.worldtradingdata.com/api/v1/history?symbol=^DAX&api_token=UFrhoimO1z70qsISJolfEH8cQFHrPsPe7LJ04ZvnwDjdgCVQ7s13Wc5KnvMU

# QUERY PARAMETERS:

# The endpoint takes up to 5 query parameters; symbol, api_token, sort_order, sort_by and output. 
# The symbol parameter allows you to request real time data for up to 500 stocks or indexes per request
# on our highest advanced plan. The output=csv parameter will return the data as a CSV format but by default will return JSON.
# The api_token is used to verify each request. 

# RAW DATA:
  
{"symbols_requested":1,"symbols_returned":1,"data":[{"symbol":"^DAX","name":"DAX PERFORMANCE-INDEX",
"currency":"N/A","price":"11944.72","price_open":"12191.41","day_high":"12207.77","day_low":"11844.88",
"52_week_high":"13596.89","52_week_low":"11726.62","day_change":"-182.97","change_pct":"-1.51",
"close_yesterday":"12127.69","market_cap":"N/A","volume":"0","volume_avg":"N/A","shares":"N/A",
"stock_exchange_long":"","stock_exchange_short":"INDEXDB","timezone":"CET","timezone_name":"Europe/Berlin",
"gmt_offset":"3600","last_trade_time":"2020-03-05 17:45:00","pe":"N/A","eps":"N/A"}]}

