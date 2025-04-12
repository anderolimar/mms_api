import sys
import os
sys.path.append(".")

import unittest
from api.services.mms import MMSService
from shared.repositories.mms import IMMSRepository
from shared.data.models.pair_mms_data import PairMMSData


class MockRepository(IMMSRepository):
    def find_mms(self, fromTms, toTms, pair):
        return [ 
            PairMMSData(pair=pair, timestamp=fromTms, mms20=1.0, mms50=2.0, mms200=3.0),
            PairMMSData(pair=pair, timestamp=toTms, mms20=4.0, mms50=5.0, mms200=6.0)
        ]

    def has_any(self):
        pass

    def insert(self, mms):
        pass              



class TestMMSService(unittest.TestCase):
    def test_get_mms_20(self):
        mockRepo = MockRepository()
        svc = MMSService(mockRepo)

        mmsList = svc.get_mms(fromTms=1, toTms=2, pair="BRLBTC", range="20")

        self.assertEqual(len(mmsList), 2)
        self.assertEqual(mmsList[0].mms, 1.0)
        self.assertEqual(mmsList[1].mms, 4.0)

    def test_get_mms_50(self):
        mockRepo = MockRepository()
        svc = MMSService(mockRepo)

        mmsList = svc.get_mms(fromTms=1, toTms=2, pair="BRLBTC", range="50")

        self.assertEqual(len(mmsList), 2)
        self.assertEqual(mmsList[0].mms, 2.0)
        self.assertEqual(mmsList[1].mms, 5.0)    

    def test_get_mms_200(self):
        mockRepo = MockRepository()
        svc = MMSService(mockRepo)

        mmsList = svc.get_mms(fromTms=1, toTms=2, pair="BRLBTC", range="200")

        self.assertEqual(len(mmsList), 2)
        self.assertEqual(mmsList[0].mms, 3.0)
        self.assertEqual(mmsList[1].mms, 6.0)       

if __name__ == "__main__":
    unittest.main()        