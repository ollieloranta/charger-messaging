FROM python:3.9

WORKDIR /code

COPY ./requirements_mqtt.txt /code/requirements.txt
COPY ./charger_messaging/mock_sender.py /code/charger_messaging/mock_sender.py
COPY ./charger_messaging/config.py /code/charger_messaging/config.py
COPY ./.env.local /code/.env.local

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code"

CMD python charger_messaging/mock_sender.py