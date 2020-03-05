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
