import requests
import json

# REQUEST_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

# yyyy-mm-dd
REQUEST_URL = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2016-01-01&end=2021-09-05"

# REQUEST_URL = "https://api.cryptowat.ch/markets/summaries"

r = requests.get(REQUEST_URL)

#full_data = r.json()['result']

#trimmed_data = {k: v for k, v in full_data.items() if k.endswith(':btcusd')}

with open('coinprices.txt', 'w') as f:
    json.dump(r.json(), f, indent=4)