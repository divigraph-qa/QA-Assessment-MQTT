# Broker Handover

## Scope

This folder owns the local Eclipse Mosquitto broker configuration used by the Compose stack.

## Implementation

- `mosquitto.conf` listens on MQTT port `1883` on all container interfaces.
- Anonymous access is enabled for local development.
- Persistence is disabled because the broker is used for transient telemetry.
- The root Compose file mounts this configuration into the `mqtt-broker` service.
- The root README documents the Compose startup command and the host connection details for QA tooling.

## Known gaps

Authentication and TLS are intentionally not configured. Add both before exposing this broker beyond a trusted local development environment.
