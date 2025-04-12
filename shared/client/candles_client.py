import requests 
from shared.config.env import API_URL
from shared.client.models import CandleResume
import logging

BTC_BRL = "BTC-BRL" 
ETH_BRL = "ETH-BRL"

BRLBTC = "BRLBTC" 
BRLETH = "BRLETH"

PAIRS = { BRLBTC: BTC_BRL, BRLETH: ETH_BRL }

class CandlesClient():

    def getCandles(self, pair, fromTms, toTms):
        list = []
        url = API_URL.replace("#pair#", pair)
        url = url.replace("#from#", str(fromTms))
        url = url.replace("#to#", str(toTms))
        
        try:
            # Make the GET request
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                candles = response.json()
                candlesTms = candles["t"]
                candlesClose = candles["c"]

                if len(candlesTms) != len(candlesClose):
                    raise Exception("Candle timestamps and closes do not match in length")

                for index, candleTms in enumerate(candlesTms):
                    list.append(CandleResume(timestamp= candleTms, close= candlesClose[index]))
            else:
                m = f"Request failed with status code {response.status_code}: {response.text}"
                logging.error(m)    
                raise Exception(m)
        except requests.exceptions.RequestException as e:
            
            logging.error(f"An error occurred: {e}")
            raise e

        return list