
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from shared.config.env import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USER
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_DATABASE}")

Session = sessionmaker(bind=engine)
