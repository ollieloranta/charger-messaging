# Charger Messaging App

Simple application for handling messages from a queue and storing them to a database.

# Installation and run with Docker

First, install [Docker](https://docs.docker.com/engine/install/) if not yet done.


Install docker-compose

```bash
sudo apt-get install docker-compose
```

Build the containers:

```bash
docker-compose build
```

Then, run the Docker environment:

```bash
docker-compose --env-file .env.localdocker up
# Or for detached mode:
docker-compose --env-file .env.localdocker up -d
```

Close program with ctrl+C, or if detached mode, use

```bash
docker-compose --env-file .env.localdocker down
```

### Reading service outputs

```bash
docker logs charger-messaging_api_1
# Or
docker logs charger-messaging_message_queue_1
```

# Usage

### Functionality

Currently the only functionality of the site is to read the values of the charger messages.

To see a raw list of all the message values, connect with your browser to the address

```
http://localhost:8000/session/
```

### API Docs

You can see the entire API Swagger documentation in the address

```
http://localhost:8000/docs
```


# (Optional) Installation without Docker

### Requirements

* An MQTT Broker running in the background (Such as [Mosquitto](http://www.steves-internet-guide.com/install-mosquitto-linux/))
* MongoDB running in the background ([Installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition))
* Conda (E.g. [Miniconda](https://docs.conda.io/en/latest/miniconda.html))

### Installing

```bash
conda create -n chargerapp python=3.9
conda activate chargerapp
pip install .
```

### Local installation Usage

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

After everything is running, you can connect to the site with your browser as shown in the section [Usage](#usage).

# Improvements

This remains a simple program with multiple possible improvements:

* Currently there is not a generalized topic management for MQTT. This should be added, 
so many different devices and sessions can easily connect. Possibly session topics would 
not need to even exist, and this would be handled only in the backend.
* The database remains quite simple, and more generalizations should be done if we 
know that many more different objects are to be added to the database.
* The Dockerfiles and docker-compose files could be optimized by looking more deeply 
for the best images to use for each service.
* Normally the .env environment file shouldn't be in Git, but this is just a simple and only locally working version.
* Provide a frontend for the website