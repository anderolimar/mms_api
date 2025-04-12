import sys
import os
sys.path.append(".")

from shared.data.db import Base, engine
from shared.data.models.pair_mms_data import PairMMSData
from shared.data.models.job import Job

# cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)