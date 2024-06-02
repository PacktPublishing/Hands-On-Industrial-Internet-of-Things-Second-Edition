FROM python
LABEL org.packt.image.authors="giacomo.veneri@gmail.com"

RUN pip install azure-iot-device
COPY SimulatedDeviceSync.py /

CMD ["python", "SimulatedDeviceSync"]