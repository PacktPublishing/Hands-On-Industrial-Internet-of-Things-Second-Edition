FROM node:alpine
LABEL org.packt.image.authors="giacomo.veneri@gmail.com"

RUN apk add --update openssl
RUN mkdir /app
WORKDIR /app
COPY package.json /app

RUN npm install
COPY . /app

EXPOSE 26543

CMD ["npm", "start"]