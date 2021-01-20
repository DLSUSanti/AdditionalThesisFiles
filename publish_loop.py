import paho.mqtt.client as mqtt
import time
import json
from random import randrange


def on_publish(client, userdata, result):
    print("data published")
    pass


client = mqtt.Client()
client.on_publish = on_publish
client.connect("localhost", 1883, 60)

while True:
    sendStringA = json.dumps({'device': 'node-1', 'IMU': [randrange(2) + 11, randrange(2) + 11, randrange(2) + 11], 'Gyro': [randrange(2) + 11, randrange(2) + 11, randrange(2) + 11]})
    sendStringB = json.dumps({'device': 'node-2', 'IMU': [randrange(100) - 49, randrange(100) - 49, randrange(100) - 49], 'Gyro': [randrange(100) - 49, randrange(100) - 49, randrange(100) - 49]})
    sendStringC = json.dumps({'device': 'node-3', 'IMU': [randrange(100) - 49, randrange(100) - 49, randrange(100) - 49], 'Gyro': [randrange(100) - 49, randrange(100) - 49, randrange(100) - 49]})
    sendStringD = json.dumps({'device': 'node-4', 'IMU': [randrange(100) - 49, randrange(100) - 49, randrange(100) - 49], 'Gyro': [randrange(100) - 49, randrange(100) - 49, randrange(100) - 49]})
    client.publish("Sensor", sendStringA)
    client.publish("Sensor", sendStringB)
    client.publish("Sensor", sendStringC)
    client.publish("Sensor", sendStringD)
    time.sleep(0.5)