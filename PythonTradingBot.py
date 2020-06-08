import alpaca_trade_api as tradeapi 
from alpaca_trade_api import StreamConn

ALPACA_BASE_URL =  "https://paper-api.alpaca.markets"

class PythonTradingBot :
    def __init__(self):
        self.alpaca = tradeapi.REST('PK6Z8BFON57U22T0SHIE', 'Z/xVVvetdAJXoE4dJkIWT0k0mwjJc2d2Q7hY6bd6', ALPACA_BASE_URL, api_version='v2')
    def run(self) :
        #On each minute 
        async def on_minute(conn, channel, bar):
            #Entry
            if bar.close >= bar.open and bar.open - bar.low > 0.1:
                print("Buying on Doji Candle!")
                self.alpaca.submit_order("MSFT", 1, 'buy', 'market', 'day')
        #Take profit at %1 increase (E.g $170 take profit at $171.7)

#connect to get streaming stock market data 
        self.conn = StreamConn('polygon key', 'polygon key here', 'wss://alpaca.socket.polygon.io/stocks')
        on_minute = self.conn(r'AM$')(on_minute)
#subscribe to Microsoft Stock
        conn.run(['AM.MSFT'])
bd = 