# Deploy Azure Iot Edge on Docker

Based on 

* https://learn.microsoft.com/en-us/azure/iot-edge/how-to-provision-single-device-linux-symmetric?view=iotedge-1.5&tabs=azure-portal%2Cubuntu
* https://github.com/Azure/Industrial-IoT/blob/main/docs/opc-publisher/readme.md

* :



## Script to deploy Azure Iot Edge runtime

    sudo apt-get -y update
    sudo apt-get -y install wget nano

    sudo wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    sudo dpkg -i packages-microsoft-prod.deb
    sudo apt-get -y update
    sudo apt-get -y upgrade
    sudo apt-get -y  install moby-engine moby-cli aziot-edge

    sudo echo {"log-driver": "local"} >> /etc/docker/daemon.json
    sudo systemctl restart docker

## Configure your iotedge
    sudo iotedge config mp --connection-string $IOTHUB_DEVICE_CONNECTION_STRING
    sudo sudo iotedge config apply

## Check status

    sudo iotedge system status
    sudo iotedge list

