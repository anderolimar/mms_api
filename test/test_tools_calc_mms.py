import sys
sys.path.append(".")

import unittest
from shared.tools.calc_mms import CalcMMS
from datetime import datetime, timedelta


class TestTimestampRange(unittest.TestCase):
    def test_timestampRangeDaysOffset(self):
        

        calcMms = CalcMMS()
        calcMms.addClose(1.0)
        calcMms.addClose(2.0)
        calcMms.addClose(3.0)
        calcMms.addClose(5.0)

        self.assertEqual(4.0, calcMms.getMMS(2))
        self.assertEqual((10.0/3), calcMms.getMMS(3))
        self.assertEqual(2.75, calcMms.getMMS(4))
    
     
if __name__ == "__main__":
    unittest.main()        