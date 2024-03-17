# MQTT Message Receiver

This project is an MQTT message receiver designed to connect to an MQTT broker, subscribe to specified topics, and save incoming messages to a local directory. It leverages the `paho-mqtt` client for managing MQTT connections and message handling in Python. Before establishing a connection to the MQTT broker, it requires connecting to a VPN using OpenVPN with a specific profile.

## Features

- VPN connection setup using OpenVPN.
- Connection to an MQTT broker with authentication.
- Subscription to multiple topics with configurable Quality of Service (QoS).
- Storage of received messages in files within a specified directory, timestamped and organized by topic.
- Basic error handling and logging for troubleshooting.

## Prerequisites

- Python 3.x.
- `paho-mqtt` library (install using `pip install paho-mqtt`).
- OpenVPN, configured with the necessary VPN profile.
- Access to an MQTT broker with valid credentials (username and password).

## Configuration

1. **VPN Setup:** Have your OpenVPN profile (`.ovpn` file) ready for connecting to the VPN. Ensure it's configured for your VPN server and authentication method.
2. **MQTT Broker Details:** Set the MQTT broker's details (`MQTT_BROKER`, `MQTT_PORT`, `MQTT_USER`, `MQTT_PASSWORD`) in the script, importing credentials from a separate module for security.
3. **Subscribed Topics:** Specify topics in the `TOPICS` list with their topic string and QoS level.
4. **Data Directory:** Define `data_directory` where messages will be saved. Ensure this directory is prepared before running the script.

## VPN Connection

Establish a VPN connection using OpenVPN and your profile before running the MQTT receiver script.

## Usage

With the VPN connection active, run the script:

```bash
python main.py
```
## Logging

Errors and exceptions are logged to `mqtt_receiver.log` in the script's directory. Ensure the log file is writable.

## Customization

You can customize the script by modifying the MQTT connection details, subscribed topics, and data directory as needed. Further customization can be achieved by altering the callback functions (`on_connect`, `on_message`, etc.) to suit your specific requirements.