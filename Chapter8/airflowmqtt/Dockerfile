FROM python:3.13.0a4

RUN pip install requests beautifulsoup4
RUN pip install paho-mqtt
RUN pip install neo4j

COPY ./config config
COPY src .

WORKDIR /
CMD ["python", "main.py"] 