import json
import os
import random
import time
from datetime import UTC, datetime

import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")

TEMP_UPPER = int(os.getenv("TEMP_UPPER_BOUND", 30))
TEMP_LOWER = int(os.getenv("TEMP_LOWER_BOUND", 20))
INTERVAL = int(os.getenv("PUBLISH_INTERVAL", 5))


def build_payload():
    return {
        "deviceId": "DEVICE001",
        "temperature": round(random.uniform(TEMP_LOWER, TEMP_UPPER), 1),
        "status": "ONLINE",
        "timestamp": datetime.now(UTC).isoformat(),
    }


def main():

    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

    print(f"Connecting to {MQTT_HOST}:{MQTT_PORT}")

    client.connect(MQTT_HOST, MQTT_PORT)
    client.loop_start()

    while True:
        payload = build_payload()

        result = client.publish(MQTT_TOPIC, json.dumps(payload), qos=1)

        print(f"Published to {MQTT_TOPIC}: {json.dumps(payload)}")

        result.wait_for_publish()

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
