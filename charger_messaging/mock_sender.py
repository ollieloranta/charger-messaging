"""Script mocking a message sender to the MQTT queue"""
import json
import time

import paho.mqtt.publish as publish

from charger_messaging.config import MQTT_URL, MQTT_PORT

TOPIC = "charger/1/connector/1/session/1"
SLEEP_TIME = 60


def main():
    message_number = 1
    while True:
        payload = {"session_id": message_number, "delivered_kWh": 30, "duration_s": 45, "cost_cents": 70}
        publish.single(TOPIC, json.dumps(payload), hostname=MQTT_URL, port=int(MQTT_PORT))
        time.sleep(SLEEP_TIME)
        message_number += 1


if __name__ == "__main__":
    main()
