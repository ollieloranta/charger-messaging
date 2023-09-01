FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements_mqtt.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./charger_messaging/message_queue.py /code/charger_messaging/message_queue.py
COPY ./charger_messaging/config.py /code/charger_messaging/config.py
COPY ./.env.local /code/.env.local

ENV PYTHONPATH "${PYTHONPATH}:/code"

CMD python -u charger_messaging/message_queue.py