from sqlalchemy import Column, Integer, Text, Float, Boolean
from shared.data.db import Base

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    pair = Column(Text, index=True)
    timestamp = Column(Integer)
    finished = Column(Boolean)
    
