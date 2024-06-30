FROM python:3.9.19
LABEL org.packt.image.authors="giacomo.veneri@gmail.com"

ARG IOTHUB_DEVICE_CONNECTION_STRING
ENV IOTHUB_DEVICE_CONNECTION_STRING=${IOTHUB_DEVICE_CONNECTION_STRING}

RUN python3 -m pip install opcua crypto cryptography azure-iot-device
COPY ./OPCUABridge.py /

CMD ["python3", "OPCUABridge.py"]