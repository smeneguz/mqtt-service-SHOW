import json
import logging
import os
from datetime import datetime
import credentials
import paho.mqtt.client as mqtt

# Define the MQTT broker details
MQTT_BROKER = "10.100.92.1"
MQTT_PORT = 3001
MQTT_USER = credentials.USER_DEV
MQTT_PASSWORD = credentials.PASSWORD_DEV

TOPICS = [("/milla_fleet/millacar06/#", 0),  # QoS level 0
          ("/milla_fleet/millacar07/#", 0)]  # QoS level 0

data_directory = "./data/"
logging.basicConfig(filename='mqtt_receiver.log', level=logging.ERROR)


# Callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        for topic, qos in TOPICS:
            print(f"Subscribing to topic: {topic} with QoS: {qos}")
            client.subscribe(topic, qos)
    else:
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    try:
        print("==============================")
        print(f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}")
        print("==============================")
        save_message(msg.topic, msg.payload.decode())
    except Exception as e:
        logging.error(f"Error handling message: {str(e)}")
        print("An error occurred while handling the message.")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed: {mid}, QoS: {granted_qos}")


def save_message(topic, payload):
    try:
        message_data = {
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "payload": json.loads(payload)
        }
    except json.JSONDecodeError:
        message_data = {
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "payload": payload
        }

    topic_name = topic.replace("/", "_").replace("#", "").replace("+", "")
    timestamp = datetime.now().strftime("%H%M%S")
    file_path = os.path.join(data_directory, f"{topic_name}_{timestamp}_messages.json")
    try:
        with open(file_path, "a") as file:
            json.dump(message_data, file)
            file.write("\n")
    except Exception as e:
        logging.error(f"Error saving message: {str(e)}")
        print("An error occurred while saving the message.")
        print(e)



client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

client.connect(MQTT_BROKER, MQTT_PORT, 120)
try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
