# edge with node-red and opc-us server

Structure of the project:
* :file_folder: node-red : edge 
* :file_folder: node-opcua-sampleserver : OPC UA Emulator
* :whale: docker-compose.yml : docker compose file to start services
* :file_folder: python-device : python device
* :whale: docker-compose-python.yml : docker compose file to start services and python devices

## Code for the Node-RED  function

    function generateGuid() { 

    return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15); 
    } 

    msg.payload = { 
    "message-id": generateGuid(), 
    "deviceId": "device1", 
    "key": "YOUR KEY", 
    "protocol": "mqtt", 
    "data": {"temperature": msg.payload} 
    } 

    return msg;

## Device client

based on https://github.com/Azure-Samples/azure-iot-samples-python