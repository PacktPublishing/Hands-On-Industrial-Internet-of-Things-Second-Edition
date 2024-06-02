cd /workdir
cp /iotedge/tools/CACertificates/*.cnf .
cp /iotedge/tools/CACertificates/certGen.sh .

./certGen.sh create_root_and_intermediate
./certGen.sh create_edge_device_identity_certificate "device1"

./certGen.sh create_edge_device_ca_certificate "iiot-book2-CA"

./certGen.sh create_device_certificate "device1-primary"
./certGen.sh create_device_certificate "device1-secondary"

openssl x509 -in certs/iot-device-device1-primary.cert.pem -fingerprint -noout
openssl x509 -in certs/iot-device-device1-secondary.cert.pem -fingerprint -noout 