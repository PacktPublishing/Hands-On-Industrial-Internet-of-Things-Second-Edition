FROM node
LABEL org.packt.image.authors="giacomo.veneri@gmail.com"

RUN apt-get install openssl
RUN mkdir /app
WORKDIR /app
COPY package.json /app

RUN npm install
COPY . /app

EXPOSE 26543

CMD ["npm", "start"]