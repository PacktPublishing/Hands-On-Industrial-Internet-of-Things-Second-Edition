FROM python:3.13.0a4

RUN pip install requests beautifulsoup4
RUN pip install paho-mqtt

COPY ./config config
COPY src .

CMD ["python", "/main.py"] 