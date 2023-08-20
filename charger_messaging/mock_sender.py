import json
import paho.mqtt.publish as publish


def main():
    MQTT_BROKER = "localhost"
    MQTT_PORT = 1883
    TOPIC = "charger/1/connector/1/session/1"

    payload = {"session_id": 1, "delivered_kWh": 30, "duration_s": 45, "cost_cents": 70}

    publish.single(TOPIC, json.dumps(payload), hostname=MQTT_BROKER, port=MQTT_PORT)


if __name__ == "__main__":
    main()
