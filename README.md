# Charger Messaging App

Simple application for handling messages from a queue and storing them to a database.

# Requirements

* An MQTT Broker (Such as [Mosquitto](http://www.steves-internet-guide.com/install-mosquitto-linux/))
* MongoDB ([Installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition))
* Conda (E.g. [Miniconda](https://docs.conda.io/en/latest/miniconda.html))

# Installation

```bash
conda create -n chargerapp python=3.11
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
