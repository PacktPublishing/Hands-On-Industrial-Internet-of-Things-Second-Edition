import json
import paho.mqtt.client as mqtt
import logging
import os
import requests
import asyncio

class STATIC:
    mapping = {}
    airflow_endpoint = None
    airflow_username = None
    airflow_password = None

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

    for topic in STATIC.mapping:
        print(f"Subscribing to {topic}")
        client.subscribe(topic)

def call(url, username,password, msg):
    headers = {"Content-type": "application/json", "Accept": "application/json"}

    try:
        with requests.session() as s:
            print(url, msg)
            response = s.post(url, 
                                data=json.dumps(msg), 
                                auth=(username, password),
                                headers=headers)
            print("Status Code", response.status_code, response.content)
    except Exception as e: 
        print("Failed",e)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    analytics = STATIC.mapping.get(msg.topic)
    if analytics:
        for analytic in analytics:
            for analytic_name in analytic:
                url = STATIC.airflow_endpoint.format(analytic=analytic_name)
                username = STATIC.airflow_username
                password = STATIC.airflow_password
                msg = { "conf": {
                    "params": analytic[analytic_name], 
                    "source": msg.topic,
                    "value" : float(msg.payload) }
                }
                
                #must be async
                print("async to", url)
                call(url=url,username=username,password=password, msg=msg)

            
# connect to the server
def connect(host, port):
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    print(f"Connecting to  {host}, {port}")
    mqttc.connect(host, port, 60)
    mqttc.loop_forever()
    

if __name__ == "__main__":
    STATIC.airflow_endpoint = os.getenv('AIRFLOW_ENDPOINT', "http://localhost:8080/api/v1/dags/{analytic}/dagRuns")
    STATIC.airflow_username = os.getenv('AIRFLOW_USERNAME', "airflow")
    STATIC.airflow_password = os.getenv('AIRFLOW_PASSWORD', "airflow")

    # Read mapping topic analytic
    config_path = os.getenv('MAPPING_CONFIG_PATH', os.path.join(os.getcwd(), '..', 'config', 'config.json'))
    with open(config_path) as f:
        STATIC.mapping = json.load(f)
    
    # start
    mqtt_host = os.getenv('MQTT_HOST', "mosquitto")
    mqtt_port = os.getenv('MQTT_PORT', 1883)
    connect(mqtt_host,mqtt_port)