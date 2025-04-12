
from shared.client.candles_client import CandlesClient
from shared.tools.timestamp_range import TimestampRange
from datetime import datetime, timedelta 
from shared.client.models import CandleResume
from shared.data.models.pair_mms_data import PairMMSData
from shared.repositories.mms import MMSRepository
from shared.tools.calc_mms import CalcMMS
import logging

class MmsLoader():

    def load(self, pairExt, pair, daysRef): 
        timestampRange = TimestampRange.timestampRangeDaysOffset(daysRef)

        ## Call candles api
        client = CandlesClient()
        candles = client.getCandles(pairExt, timestampRange.fromTms, timestampRange.toTms)
        candles.sort(key=lambda x: x.timestamp, reverse=False)
        logging.info(f"candles = {len(candles)} for {pair}")

        ## calculate datetime references
        map = {}
        now = datetime.now()
        today = datetime(year= now.year, month= now.month, day= now.day)
        yesterday = today - timedelta(seconds= 1)
        maxDatetime =  yesterday - timedelta(days= daysRef)

        repo = MMSRepository()

        # Map candles closes by date
        for candle in candles:
            self.updateMap(map, candle, today, maxDatetime)

        logging.info(f"map(years) = {len(map)}")
        
        # Insert mms data
        for k in map :
            for k2 in map[k]:
                for k3 in map[k][k2]:
                    pairMMs = PairMMSData()
                    pairMMs.pair = pair
                    pairMMs.timestamp = datetime(year=k, month=k2, day=k3).timestamp()
                    pairMMs.mms20 = map[k][k2][k3].getMMS(20)
                    pairMMs.mms50 = map[k][k2][k3].getMMS(50)
                    pairMMs.mms200 = map[k][k2][k3].getMMS(200)
                    repo.insert(pairMMs)   
 
        logging.info(f"Finish insert mms data for {pair}")         


    def updateMap(self, map: map, candle: CandleResume, today, maxDatetime):
        closeDatetime = datetime.fromtimestamp(candle.timestamp)

        for i in range(0,200):
            dateRef = closeDatetime + timedelta(days= i)
            if dateRef < maxDatetime or dateRef > today:
                continue

            if map.get(dateRef.year) is None:
                map[dateRef.year] = map.get(dateRef.year, {})

            if map[dateRef.year].get(dateRef.month) is None:    
                map[dateRef.year][dateRef.month] = map[dateRef.year].get(dateRef.month, {})
            
            if map[dateRef.year][dateRef.month].get(dateRef.day) is None:
                map[dateRef.year][dateRef.month][dateRef.day] = map[dateRef.year][dateRef.month].get(dateRef.day, CalcMMS())
            
            map[dateRef.year][dateRef.month][dateRef.day].addClose(float(candle.close))

