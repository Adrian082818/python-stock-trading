import alpaca_trade_api as tradeapi 
from alpaca_trade_api import StreamConn
import threading
import time
import datetime
import logging
import argparse

#initialize logging to see debug output
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True 

ALPACA_BASE_URL =  "https://paper-api.alpaca.markets"

class PythonTradingBot :
#this method sets up the REST API
    def __init__(self):
        self.alpaca = tradeapi.REST('PK6Z8BFON57U22T0SHIE', 'Z/xVVvetdAJXoE4dJkIWT0k0mwjJc2d2Q7hY6bd6', ALPACA_BASE_URL, api_version='v2')
    def run(self) :
        #On each minute 
        async def on_minute(conn, channel, bar):
            #Entry
            symbol = bar.symbol
            print("Close: ", bar.close)
            print("Open: ", bar.open)
            print("Low: ", bar.low)
            print(symbol)
            #Check for Doji
            if bar.close > bar.open and bar.open - bar.low > 0.1:
                print("Buying on Doji Candle!")
                self.alpaca.submit_order(symbol, 1, 'buy', 'market', 'day')
        #Take profit at %1 increase (E.g $170 take profit at $171.7)

        #connect to get streaming stock market data 
        self.conn = StreamConn('polygon key', 'polygon key here', 'wss://alpaca.socket.polygon.io/stocks')
        on_minute = conn.on(r'AM$')(on_minute)

        #subscribe to Microsoft Stock
        conn.run(['AM.MSFT'])
#Run the BuyDoji class
bd = PythonTradingBot()
bd.run()