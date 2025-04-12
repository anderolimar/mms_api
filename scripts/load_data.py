import sys
import os
sys.path.append(".")

from shared.repositories.mms import MMSRepository
from shared.repositories.jobs import JobsRepository
from shared.tools.mms_loader import MmsLoader
from datetime import datetime, timedelta
from shared.data.models.job import Job
from shared.client.candles_client import PAIRS
import logging

def run(): 
    try:
        repo = MMSRepository()
        if repo.has_any():
                return
        
        for pair in PAIRS:
            MmsLoader().load(PAIRS[pair], pair, 365)

            now = datetime.now() 
            nowRef = datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=0)
            tomorrow = nowRef + timedelta(days=1)
            
            job = Job()
            job.pair = pair
            job.timestamp = tomorrow.timestamp()
            job.finished = False

            jobRepo = JobsRepository()
            jobRepo.insert(job)   

    except Exception as e:
        logging.error(f"Error on run: {e}")
        raise e

run()    

