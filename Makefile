.PHONY: test

install:
	pip install -r requirements.txt

virtual:
	python3 -m venv .venv
	
active:
	sh .venv/bin/activate	

start:
	fastapi dev ./api/main.py

load:
	python3 ./scripts/load_data.py 	

job:
	python3 ./jobs/load_data.py

setup:
	python3 ./shared/data/setup.py

env-up:
	docker-compose up -d	

env-down:
	docker-compose down

test:
	python3 -m unittest

up-db:
	docker-compose up -d db	

down-db:
	docker-compose down db	

