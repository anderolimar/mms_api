from sqlalchemy import Column, Integer, Text, Float
from shared.data.db import Base

class PairMMSData(Base):
    __tablename__ = "pair_mms"
    id = Column(Integer, primary_key=True)
    pair = Column(Text, index=True)
    timestamp = Column(Integer, index=True)
    mms20 = Column(Float)
    mms50 = Column(Float)
    mms200 = Column(Float)
    
