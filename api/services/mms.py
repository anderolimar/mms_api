from abc import ABC, abstractmethod
from shared.repositories.mms import IMMSRepository
from api.models.response.data import MMSData
import logging 

class IMMSService(ABC):
    @abstractmethod
    def get_mms(self, fromTms, toTms, pair, range): 
        pass


class MMSService(IMMSService):
    def __init__(self, repo: IMMSRepository):
        self.repo = repo

    def get_mms(self, fromTms, toTms, pair, range):
        try:
            logging.info(f"get_mms: fromTms={fromTms}, toTms={toTms}, pair={pair}, range={range}")
            db_mms_list = self.repo.find_mms(fromTms, toTms, pair)   

            # logging.info(f"get_mms find: {len(db_mms_list)}")

            mms_list = []

            for mms in db_mms_list :
                mmsdata = MMSData()
                mmsdata.timestamp = mms.timestamp
                match str(range):
                    case "20":
                        mmsdata.mms = mms.mms20
                    case "50":
                        mmsdata.mms = mms.mms50
                    case "200":
                        mmsdata.mms = mms.mms200
                
                mms_list.append(mmsdata)


            return mms_list
        except Exception as e:
            logging.error(f"Error in get_mms: {e}")
            raise e
