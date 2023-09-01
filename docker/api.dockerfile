FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements_api.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./charger_messaging /code/charger_messaging
COPY ./.env.local /code/.env.local

ENV PYTHONPATH "${PYTHONPATH}:/code"

CMD python -u charger_messaging/api.py