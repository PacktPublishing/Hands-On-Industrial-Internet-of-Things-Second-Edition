work with Docker
================
create a file called Dockerfile; Finally copy into the file the following command-line instructions: 

    FROM	alpine 

    # Install python3 

    RUN apk add --update python3 

    # Copy html 

    RUN mkdir /src ADD static/ /src RUN cd /src 

    # Run http server on port 8080 

    EXPOSE	8080 

    CMD ["python3", "-m", "http.server", "8080"] 

 

From the command console, you have to build a simple HTML page called index.html: 

    mkdir static 

    echo "<html><body>IIoT</body></html>" > static/index.html 

  

Now follow these steps: 

Build your Docker container with the following command: 

    docker build --tag micropy . 

Run your Docker container: 

    docker run -p 80:8080 micropy 


work with TSDB
==============
Create data directory:

    mkdir data

Build the 2 images:

    docker compose build 

The we can start the 3 servers using: 

    docker compose up 



