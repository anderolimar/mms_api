import sys
sys.path.append(".")

import unittest
from shared.tools.timestamp_range import TimestampRange
from datetime import datetime, timedelta


class TestTimestampRange(unittest.TestCase):
    
    def test_timestampRangeDaysOffset(self):
        dateref = datetime(year= 2025, month= 4, day= 1)
        
        days = 10
        
        expectedTo = dateref - timedelta(seconds= 1)
        expectedFrom = dateref - timedelta(days=days + 200)

        timestampRange = TimestampRange.timestampRangeDaysOffset(days, now=dateref)

        self.assertEqual(timestampRange.fromTms, int(expectedFrom.timestamp()))
        self.assertEqual(timestampRange.toTms, int(expectedTo.timestamp()))
    
     
if __name__ == "__main__":
    unittest.main()        