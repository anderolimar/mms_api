import os
from dotenv import load_dotenv
load_dotenv(dotenv_path= os.path.join(os.path.dirname(__file__), '../../.env'))


DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_DATABASE = os.environ.get('DB_DATABASE')
API_URL = os.environ.get('API_URL')


