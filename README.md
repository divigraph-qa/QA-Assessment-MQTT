# QA Assignment
### *** The assignment questions can be found in the `tests/README.md` file. The rest of this file is an overview of the entire project. *** <br><br><br>

# MQTT Docker Service

This project starts two services:

- An Eclipse Mosquitto MQTT broker.
- A Python publisher (Simulated Service) that sends temperature telemetry.

## Prerequisites

Install and start Docker. You do not need to install Python, `uv`, or Mosquitto on your computer.

## Start the service

Run these steps from the repository root, the folder containing `docker-compose.yaml`:

1. Open `publisher/.env` and replace `your_name` in `MQTT_TOPIC` with your identifier. For example:
	```text
	MQTT_TOPIC=assessment/alex/telemetry
	```

	If `publisher/.env` does not exist, copy `publisher/.env.example` to `publisher/.env` first.
2. Start the broker and publisher:
	```powershell
	docker compose up --build
	```

That is the complete service setup. The broker will now be available from the host at `localhost:1883`.<br>
The first run may take a few minutes while Docker downloads the broker image and builds the publisher image. Keep this terminal open while testing.<br>
The publisher connects to the broker automatically and publishes one message every 5 seconds by default.

To stop the service, press `Ctrl+C`. To remove the stopped containers, run this from the repository root:
```powershell
docker compose down
```

## View messages with MQTT Explorer

MQTT Explorer is optional, but it is useful for checking that messages are arriving.

Create a connection with:

- Host: `localhost`
- Port: `1883`
- TLS: disabled
- Authentication: disabled

Subscribe to the topic in `publisher/.env`, or subscribe to `#` to see all topics.


## Project layout
- `docker-compose.yaml` starts the broker and publisher together.
- `broker/` contains the Mosquitto configuration.
- `publisher/` contains the publisher, Dockerfile, and environment settings.
- `tests/` is reserved for the QA test framework and automated tests.