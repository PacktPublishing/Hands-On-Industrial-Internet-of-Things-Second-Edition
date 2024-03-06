# data flow with mqtt server, telegraf and influxdb

Structure of the project:
* 📁 mosquitto : MQTT data broker
* 📁 telegraf : configuration to inject data from MQTT data broker to InfluxDB
* docker-compose.yml : docker compose file to start services (InfluxDB, Mosquitto, Telegraf)
