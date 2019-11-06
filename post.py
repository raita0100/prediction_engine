import requests
import json

url = "https://predict-stock.onrender.com/"

querystring = {"0":"GOOGL","1":"AAPL","2":"AMZN","3":"SBUX","4":"NFLX","5":"FB"}

headers = {
    'cache-control': "no-cache",
    'Content-Type': "application/json",
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)
