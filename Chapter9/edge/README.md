# edge with node-red and opc-us server

Structure of the project:
* :file_folder: node-red : edge with AWS IOT Support 
* :file_folder: node-opcua-sampleserver : OPC UA Emulator
* :file_folder: certificates : folder where to save certificates
* :whale: docker-compose.yml : docker compose file to start services
* :whale: docker-compose-greengrass.yml : docker compose file to start greengrass
* :whale: docker-compose-device.yml : docker compose file to start device based on AWS SDK


## Policy example

    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": [
            "iot:Publish",
            "iot:Receive",
            "iot:PublishRetain"
        ],
        "Resource": [
            "arn:aws:iot:eu-central-1:533267170573:topic/sdk/test/python",
        ]
        },
        {
        "Effect": "Allow",
        "Action": [
            "iot:Subscribe"
        ],
        "Resource": [
            "arn:aws:iot:eu-central-1:533267170573:topicfilter/sdk/test/python"
        ]
        },
        {
        "Effect": "Allow",
        "Action": [
            "iot:Connect"
        ],
        "Resource": [
            "arn:aws:iot:eu-central-1:533267170573:client/device1"
        ]
        }
    ]
    }

# Grengrass commnd

## Run greengrass on docker

     docker network create iiot-book-2-net-edge 

     docker run --rm -it --network iiot-book-2-net-edge amazonlinux:2023 /bin/bash 

Then install unzip and curl. From docker bash run the following command to install java, curl and unzip: 

     apt-get update && apt-get install –y unzip wget sudo shadow-utils less systemd systemd-sysv kernel-libbpf which procps-ng java 

Export credentials:

To get temporary credentials run the following command: 

     aws sts get-session-token --duration-seconds 1800

or from cloudhsell
     curl -H "Authorization: $AWS_CONTAINER_AUTHORIZATION_TOKEN" $AWS_CONTAINER_CREDENTIALS_FULL

then replace on:

     export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> 
     export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> 
     export AWS_SESSION_TOKEN=<AWS_SESSION_TOKEN> 


Start greengrass:

      java -Droot="/greengrass/v2" -Dlog.store=FILE -jar ./GreengrassInstaller/lib/Greengrass.jar --aws-region eu-central-1 --thing-name GreengrassDevice1 --thing-group-name GreengrassQuickStartGroup --component-default-user ggc_user:ggc_group --provision true --setup-system-service false --deploy-dev-tools true

## Run greengrass with docker compose

Change the access key on docker-compose-greengrass.yml

      docker compose -f .\docker-compose-greengrass.yml up -d