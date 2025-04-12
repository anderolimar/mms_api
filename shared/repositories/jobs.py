from abc import ABC, abstractmethod
from shared.data.models.job import Job
from shared.data.db import Session

class IJobsRepository(ABC):
    @abstractmethod
    def insert(self, job: Job):
        pass

    @abstractmethod
    def find_jobs(self, pair): 
        pass

class JobsRepository(IJobsRepository):
    def insert(self, job: Job):
        with Session() as session:
            session.add(job)
            session.commit()  


    def find_jobs(self, pair): 
        list = []
        with Session() as session:
            jobs = session.query(Job).where(Job.pair == pair).where(Job.finished == False)
            list = jobs
        return list            

