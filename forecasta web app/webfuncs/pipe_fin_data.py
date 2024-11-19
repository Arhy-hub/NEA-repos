import requests 
import json
import pg8000
from SQLqueries import already_exists, conditional_insert_data

api_key = "KLHEIVZHOMAM9FRW"

#function which fetches ticker data
# format is {symbol,open,high,low,price,volume,latest trading day, previous close, change, percent change}
# format i need {assetname,assettype,assetvalue,assetpricechange,volume}
#i need to extract symbol,price,volume,%change
#then perform a symbol search and add to the list so
#pass the 

def fetch_ticker_data(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json() 
    return print(data)

def store_ticker_data(data):
    if already_exists("assets","asset_id",data[0]) == True:
        pass
    else:
        pass
    return 

def ticker_type(symbol):
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data[2]
#we have stock data now --> we want to store in db 
# to store in db check if it already exists other wise store


#we wanna store the data and pipeline the data
#Alpha vantage sends data as json --> 
#json is converted and parsed to store in db  -->
#data is then sent to webpage as json and then parsed at client side

fetch_ticker_data("AAPL")