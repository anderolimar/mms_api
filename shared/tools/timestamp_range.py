from datetime import datetime, timedelta

class TimestampRange():
    def __init__(self, fromTms: int, toTms: int):
        self.fromTms = fromTms
        self.toTms = toTms
    
    @staticmethod
    def timestampRangeDaysOffset(days, now = datetime.now()):
        daysLimit = days + 200
        today = datetime(year= now.year, month= now.month, day= now.day)
    
        dayTo = today - timedelta(seconds= 1)
        dayFrom = today - timedelta(days=daysLimit)

        fromTms = datetime.timestamp(dayFrom)
        toTms = datetime.timestamp(dayTo)
        return TimestampRange(fromTms=int(fromTms), toTms= int(toTms))
