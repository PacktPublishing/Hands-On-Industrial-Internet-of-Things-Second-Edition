FROM python:3.9 

RUN pip install requests beautifulsoup4
RUN pip install paho-mqtt

ADD src/main.py .
CMD ["python", "./main.py"] 