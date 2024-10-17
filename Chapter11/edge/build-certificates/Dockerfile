FROM alpine/openssl

RUN apk add git bash ncurses
RUN git clone https://github.com/Azure/iotedge.git

COPY build.sh /build.sh
RUN chmod +x /build.sh


CMD ["/bin/bash"]