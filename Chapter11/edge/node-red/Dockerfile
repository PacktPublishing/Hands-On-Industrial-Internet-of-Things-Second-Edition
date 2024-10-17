FROM nodered/node-red
LABEL org.packt.image.authors="giacomo.veneri@gmail.com"

RUN npm install node-red-contrib-azure-iot-hub
RUN npm install node-red-contrib-opcua

EXPOSE 1880

CMD ["npm", "start"]