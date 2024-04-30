FROM python:3.9.19

ARG AWS_REGION
ARG AWS_DEVICE_NAME
ARG AWS_DEVICE_TOPIC
ARG AWS_IOT_ENDPOINT

ENV AWS_REGION=${AWS_REGION}
ENV AWS_DEVICE_NAME=${AWS_DEVICE_NAME}
ENV AWS_DEVICE_TOPIC=${AWS_DEVICE_TOPIC}
ENV AWS_IOT_ENDPOINT=${AWS_IOT_ENDPOINT}

RUN apt-get update && apt-get install -y git curl

RUN curl https://www.amazontrust.com/repository/AmazonRootCA1.pem > root-CA.crt

RUN git clone https://github.com/aws/aws-iot-device-sdk-python-v2.git --recursive
RUN python3 -m pip install ./aws-iot-device-sdk-python-v2
RUN python3 -m pip install opcua crypto cryptography

RUN echo "#/bin/bash" > /start.sh
RUN echo "python3 /samples/pubsub_opcua.py --endpoint ${AWS_IOT_ENDPOINT} --ca_file root-CA.crt --cert /certificates/${AWS_DEVICE_NAME}.cert.pem --key /certificates/${AWS_DEVICE_NAME}.private.key --client_id ${AWS_DEVICE_NAME} --topic ${AWS_DEVICE_TOPIC} --count 0" >> /start.sh
RUN chmod +x /start.sh
CMD ["/bin/bash", "-c" , "/start.sh"]
#CMD ["/bin/bash"]

