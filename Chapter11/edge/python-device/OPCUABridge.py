# Licensed under the MIT license. See LICENSE file in the project root for full license information.
# Based on https://github.com/Azure/azure-iot-sdk-python/samples

import os,random,time, sys, datetime, opcua, uuid, asyncio, json
from azure.iot.device import Message
from azure.iot.device.aio import IoTHubModuleClient

async def send_telemetry(clientOPCUA, clientIOT, msg_data_format='{{"temperature": {temperature},"cpu": {cpu}}}'):
    # getting a variable node using its browse path
    myvarC = clientOPCUA.get_node("ns=1;s=CPU").get_value()
    myvarT = clientOPCUA.get_node("ns=1;s=Temperature").get_value()
    msg_data_formatted = msg_data_format.format(temperature=myvarT, cpu=myvarC)
    message = Message(data = msg_data_formatted,
                      content_encoding='utf-8',
                      content_type='application/json',
                      message_id=str(uuid.uuid4()))


    # Add a custom application property to the message.
    # An IoT hub can filter on these properties without access to the message body.
    if myvarC > 99:
        message.custom_properties["CPUAlert"] = "true"
    else:
        message.custom_properties["CPUAlert"] = "false"

    # Send the message.
    print(f"Sending message: {message.data} {message.custom_properties}")
    await clientIOT.send_message(message)
    print("Message successfully sent")
        


async def main():
    print("Starting OPCUA Bridge")

    # You can use the Azure CLI to find the connection string:
    # az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
    CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

    # Instantiate the IOT client.
    clientIOT = IoTHubModuleClient.create_from_connection_string(CONNECTION_STRING)
    await clientIOT.connect()
    print("Connected to Azure IOT Hub")

    # Connect OPC UA Server
    print('wait 15 seconds')
    time.sleep(15)
    try:
        print("connect to localhost")
        clientOPCUA = opcua.Client("opc.tcp://localhost:26543")
        clientOPCUA.connect()
    except Exception as e:
        print(e)
        print("connect to opc-ua-server")
        clientOPCUA = opcua.Client("opc.tcp://opc-ua-server:26543")
        clientOPCUA.connect()
    print("Connected to OPCUA SERVER")

    # Run Sample
    try:
        while True:
            await asyncio.gather(send_telemetry(clientOPCUA, clientIOT))
            time.sleep(10)
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped by user")
    finally:
        # Upon application exit, shut down the client
        print("Shutting down IoTHubClient")
        clientIOT.shutdown()

if __name__ == '__main__':
    asyncio.run(main())