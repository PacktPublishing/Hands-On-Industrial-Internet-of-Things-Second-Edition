node-opcua-sampleserver
=======================

A simple OPC-UA server based on node-opcua

based on 
https://github.com/node-opcua/node-opcua-sampleserver


How To
------

    git clone https://github.com/PacktPublishing/Hands-On-Industrial-Internet-of-Things-Second-Edition.git 

    cd Hands-On-Industrial-Internet-of-Things-Second-Edition 

    cd Chapter6 

    npm install  

    npm start


Start node-red docker container
===============================

    mkdir data 

    docker run -it -p 1880:1880 -v data:/data --name mynodered nodered/node-red 

On a separate comman line 

    docker exec -it mynodered npm install node-red-contrib-opcua 

    docker commit mynodered nodered/node-red-opc 

Close the running docker and start a new docker container with the new image: 

    docker run -it -p 1880:1880 -v data:/data --name mynodered nodered/node-red-opc 




