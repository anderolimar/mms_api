
FROM python:3.13-alpine


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code/api

COPY ./shared /code/shared


CMD ["fastapi", "run", "api/main.py", "--port", "80"]