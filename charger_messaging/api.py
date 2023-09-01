import uvicorn
from charger_messaging.config import API_URL, API_PORT

if __name__ == "__main__":
    uvicorn.run("server.app:app", host=API_URL, port=int(API_PORT))
