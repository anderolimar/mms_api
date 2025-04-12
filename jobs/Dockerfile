FROM python:3.13-alpine


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./jobs /code/jobs

COPY ./shared /code/shared


CMD ["python3", "jobs/load_data.py"]