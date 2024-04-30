# grengrass

## build linux container for greengrass
     docker compose -f .\docker-compose-awsiot.yml build
     docker exec edge-greengrass-1 /bin/bash

## run greengrass
     sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE -jar ./GreengrassInstaller/lib/Greengrass.jar --aws-region eu-central-1 --thing-name GreengrassDevice1 --thing-group-name GreengrassQuickStartGroup --component-default-user ggc_user:ggc_group --provision true --setup-system-service false --deploy-dev-tools true

## Auth policy
{
  "deviceGroups": {
    "formatVersion": "2021-03-05",
    "definitions": {
      "MyPermissiveDeviceGroup": {
        "selectionRule": "thingName: *",
        "policyName": "MyPermissivePolicy"
      }
    },
    "policies": {
      "MyPermissivePolicy": {
        "AllowAll": {
          "statementDescription": "Allow client devices to perform all actions.",
          "operations": [
            "*"
          ],
          "resources": [
            "*"
          ]
        }
      }
    }
  }
}

## MQTT BRIDGE
{
  "mqttTopicMapping": {
    "ClientDeviceHelloWorld": {
      "topic": "clients/device1/#",
      "source": "LocalMqtt",
      "target": "IotCore"
    }
  }
}