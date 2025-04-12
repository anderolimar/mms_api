class CalcMMS:
    def __init__(self):
        self.closes = []

    def addClose(self, close):  
        self.closes.append(close)

    def getMMS(self, range):
        if range > len(self.closes):
            return sum(self.closes) / len(self.closes) 
        idx = len(self.closes) - range     
        return sum(self.closes[idx:]) / range