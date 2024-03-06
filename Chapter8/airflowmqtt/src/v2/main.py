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


from neo4j import GraphDatabase

class Neo4JClient:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query):
        with self.driver.session() as session:
            ret = session.run(query)
            return ret.data()

class Neo4JConfigParser(Neo4JClient):

    def get_config(self):
        ret = {}
        measures = self.query('MATCH (M:Measure)-[BELONGING_OF]->(A) RETURN M.name, M.topic, M.threshold, M.analytic, A.name')
        for i in measures:
            topic = i["M.topic"]
            if topic is not None:
                ret[topic] =[
                    {i["M.analytic"]: {"asset": i["M.name"], "threshold":i["M.threshold"]}}
                    ]
        return ret

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
    mqttc.connect(host, port, 60)
    mqttc.loop_forever()
    

if __name__ == "__main__":
    print("MQTT to Airflow trigger Service")
    STATIC.airflow_endpoint = os.getenv('AIRFLOW_ENDPOINT', "http://localhost:8080/api/v1/dags/{analytic}/dagRuns")
    STATIC.airflow_username = os.getenv('AIRFLOW_USERNAME', "airflow")
    STATIC.airflow_password = os.getenv('AIRFLOW_PASSWORD', "airflow")

    # Read mapping topic analytic
    neo4j_url = os.getenv('NEO4J_ENDPOINT', None)
    neo4j_username = os.getenv('NEO4J_USERNAME', "neo4j")
    neo4j_password = os.getenv('NEO4J_PASSWORD', "admin")
    if neo4j_url is not None:
        config = Neo4JConfigParser(neo4j_url, neo4j_username, neo4j_password)

        STATIC.mapping = config.get_config()
        config.close
    else:
        config_path = os.getenv('MAPPING_CONFIG_PATH', os.path.join(os.getcwd(), '..', 'config', 'config.json'))
        with open(config_path) as f:
            STATIC.mapping = json.load(f)
    
    print(f"Mappping {STATIC.mapping}")
    
    # start
    mqtt_host = os.getenv('MQTT_HOST', "mosquitto")
    mqtt_port = os.getenv('MQTT_PORT', 1883)
    print(f"Connecting to  {mqtt_host}, {mqtt_port}")
    connect(mqtt_host,mqtt_port)