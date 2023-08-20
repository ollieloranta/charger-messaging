# Charger Messaging App

Simple application for handling messages from a queue and storing them to a database.

# Installation and run with Docker

Optionally, create a conda environment, then install docker-compose.

```bash
pip install docker-compose
```

Then, run the Docker environment:

```bash
docker-compose up
# Or for detached mode:
docker-compose up -d
```

# Installation without Docker

### Requirements

* An MQTT Broker running in the background (Such as [Mosquitto](http://www.steves-internet-guide.com/install-mosquitto-linux/))
* MongoDB ([Installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition))
* Conda (E.g. [Miniconda](https://docs.conda.io/en/latest/miniconda.html))

### Installing

```bash
conda create -n chargerapp python=3.9
conda activate chargerapp
pip install .
```

# Usage

In separate terminals, run the three services:

### 1. FastAPI Backend
```bash
python charger_messaging/api.py
```

### 2. MQTT Broker
```bash
python charger_messaging/message_queue.py
```

### 3. Mock message sender
```bash
python charger_messaging/mock_sender.py
```
