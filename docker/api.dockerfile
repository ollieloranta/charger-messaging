FROM python:3.9

WORKDIR /code

COPY ./requirements_api.txt /code/requirements.txt
COPY ./charger_messaging /code/charger_messaging
COPY ./.env.local /code/.env.local

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code"

CMD python charger_messaging/api.py