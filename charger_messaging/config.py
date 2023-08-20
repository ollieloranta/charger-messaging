from dotenv import load_dotenv
import os


load_dotenv(".env.local")

DATABASE_URL = os.getenv("DATABASE_URL")

API_URL = os.getenv("API_URL")
API_PORT = os.getenv("API_PORT")
API_ADDRESS = f"http://{API_URL}:{API_PORT}"

MQTT_URL = os.getenv("MQTT_URL")
MQTT_PORT = os.getenv("MQTT_PORT")
