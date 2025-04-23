from abc import ABC, abstractmethod
from shared.data.models.pair_mms_data import PairMMSData
from shared.data.db import Session

class IMMSRepository(ABC):
    @abstractmethod  
    def has_any(self): 
        pass
    
    @abstractmethod
    def insert(self, pairMMS: PairMMSData):
        pass

    @abstractmethod
    def find_mms(self, fromTms, toTms, pair):
        pass

class MMSRepository(IMMSRepository):
    def has_any(self): 
        with Session() as session:
            pairMms = session.query(PairMMSData).get(1)
            if pairMms != None :
                return True
        return False
    

    def insert(self, pairMMS: PairMMSData):
        with Session() as session:
            session.add(pairMMS)
            session.commit()  


    def find_mms(self, fromTms, toTms, pair): 
        list = []
        with Session() as session:
            pairMms = session.query(PairMMSData).where(PairMMSData.pair == pair).where(PairMMSData.timestamp >= fromTms).where(PairMMSData.timestamp <= toTms)
            list = pairMms

        return list            

