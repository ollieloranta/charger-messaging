FROM python:3.9-slim

WORKDIR /code

COPY ./requirements_mqtt.txt /code/requirements.txt
COPY ./charger_messaging/message_queue.py /code/charger_messaging/message_queue.py
COPY ./charger_messaging/config.py /code/charger_messaging/config.py
COPY ./.env.local /code/.env.local

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code"

CMD python -u charger_messaging/message_queue.py