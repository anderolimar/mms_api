import sys
import os
sys.path.append(".")

from shared.repositories.jobs import JobsRepository
from shared.data.models.job import Job
from shared.client.candles_client import PAIRS
from shared.tools.mms_loader import MmsLoader
import schedule as scheduler
from datetime import datetime, timedelta
import time
import logging

# Configure logging 
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("load_data.log"),
#         logging.StreamHandler()
#     ]
# )

def execute():
    repo = JobsRepository()
    for pair in PAIRS:
        jobs = repo.find_jobs(pair)

        logging.info(f"Find {str(len(jobs))} job(s) to run")

        for job in jobs:
            if job.finished is False:
                refDate = datetime.fromtimestamp(job.timestamp)
                delta = datetime.now() - refDate
                days = delta.days

                MmsLoader().load(PAIRS[pair], pair, days)

                now = datetime.now() 
                nowRef = datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=0)
                tomorrow = nowRef + timedelta(days=1)

                job = Job()
                job.pair = pair
                job.timestamp = tomorrow.timestamp()
                job.finished = False

                repo.insert(job) 

                logging.info(f"Finish job to pair : {pair}")

def run():
    try:
        execute()  
    except Exception as e:
        logging.error(f"Error on run: {e}")
        scheduler.every(10).seconds.do(retry)

def retry():
    try:
        execute()     
        return scheduler.CancelJob   
    except Exception as e:
        logging.error(f"Error on retry: {e}")


# Schedule the job every day at a specific time
scheduleHour = os.getenv("SCHEDULE_HOUR", "06:00")
scheduler.every().day.at(scheduleHour).do(run)

while True:
    scheduler.run_pending()
    time.sleep(1)

