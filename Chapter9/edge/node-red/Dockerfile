FROM nodered/node-red
LABEL org.packt.image.authors="giacomo.veneri@gmail.com"

RUN npm install node-red-contrib-opcua 
RUN npm install node-red-contrib-aws-iot-hub 


EXPOSE 1880

CMD ["npm", "start"]