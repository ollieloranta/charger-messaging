"""Paho-MQTT queue which sends message contents to be handled by FastAPI"""
import logging
import requests

import paho.mqtt.client as mqtt

from charger_messaging.config import MQTT_URL, MQTT_PORT, API_ADDRESS

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')
logger = logging.getLogger("MQTT")


def on_connect(client, userdata, flags, rc):
    logger.info("Connected to MQTT Broker with code: " + str(rc))
    # Dummy topic that would be independent of specific device or session IDs
    client.subscribe("charger/1/connector/1/session/1")


def on_message(client, userdata, msg):
    """When receiving a message, send it to the API to be stored.
    Message sending fails if data is incorrect or API is not available.
    """
    message = msg.payload.decode('utf-8')
    logger.info(f"Received message: {message}")
    try:
        requests.post(f"{API_ADDRESS}/session/", data=message)
        logger.info(f"Message sent to API.")
    except requests.exceptions.ConnectionError:
        logger.error(f"No connection to API.")
    except requests.exceptions.InvalidSchema:
        logger.error(f"Invalid API specifications. Check the .env file.")
    except Exception as err:
        logger.error(err)


def main():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_URL, int(MQTT_PORT), 60)
    mqtt_client.loop_forever()


if __name__ == "__main__":
    main()
