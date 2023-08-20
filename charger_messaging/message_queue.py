import json
import requests

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with code: " + str(rc))
    client.subscribe("charger/1/connector/1/session/1")


def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    try:
        requests.post("http://localhost:8000/session/", json=message)
    except Exception as err:
        print("Error: ", err)


def main():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect("localhost", 1883, 60)
    mqtt_client.loop_forever()


if __name__ == "__main__":
    main()
