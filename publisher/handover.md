# Publisher Handover

## Scope

This folder owns the Python MQTT telemetry publisher and its `uv` dependency environment.

## Implementation

- `mqtt-publisher.py` publishes JSON telemetry at the configured interval.
- `pyproject.toml` and `uv.lock` define the dependencies managed by Astral's `uv`.
- `Dockerfile` builds the publisher image from this folder as its Docker build context.
- `.env` is used for local execution; Compose overrides `MQTT_HOST` to `mqtt-broker` for container-to-container networking.
- `.env.example` documents the required publisher settings without local machine-specific values.
- The root README documents Compose as the setup path and defines the telemetry checks expected from the QA test framework.

## Known gaps

The publisher assumes the broker is available when it starts. Compose orders the services but does not wait for broker readiness; restart behavior handles transient startup failures.
