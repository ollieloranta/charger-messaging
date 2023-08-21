"""Script with very simple logic mocking a message sender to the MQTT queue"""
import json
import time

import paho.mqtt.publish as publish

from charger_messaging.config import MQTT_URL, MQTT_PORT

TOPIC = "charger/1/connector/1/session/1"  # Dummy topic that would change per device and session
START_WAIT = 5  # How many seconds to wait before sending first message
SLEEP_TIME = 3  # How often to send mock messages
MAX_TIME = 100  # Limit if mock is accidentally left open


def main():
    time.sleep(START_WAIT)
    message_number = 1
    start_time = time.time()
    while True:
        if time.time() - start_time > MAX_TIME:
            # Mock program has run long enough
            return
        # Dummy value to be sent
        payload = {"session_id": message_number, "delivered_kWh": 30, "duration_s": 45, "cost_cents": 70}
        publish.single(TOPIC, json.dumps(payload), hostname=MQTT_URL, port=int(MQTT_PORT))
        time.sleep(SLEEP_TIME)
        message_number += 1


if __name__ == "__main__":
    main()
