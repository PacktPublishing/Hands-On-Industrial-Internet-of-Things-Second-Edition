# Hands-On Industrial Internet of Things- Second Edition

<a href="https://www.packtpub.com/en-us/product/hands-on-industrial-internet-of-things-9781835887462?utm_source=github&utm_medium=repository&utm_campaign=9781786461629"><img src="https://content.packt.com/_/image/xxlarge/B22127/cover_image.jpg" alt="" height="256px" align="right"></a>

This is the code repository for [Hands-On Industrial Internet of Things- Second Edition](https://www.packtpub.com/en-us/product/hands-on-industrial-internet-of-things-9781835887462?utm_source=github&utm_medium=repository&utm_campaign=9781786461629), published by Packt.

**Build robust industrial IoT infrastructure by using the cloud and artificial intelligence**

## What is this book about?
This book shows you how to develop on-premise architecture, build AI analytics, and leverage AWS and Azure cloud to create your Industrial Internet of Things (IIoT) platform.

This book covers the following exciting features:
* Get a solid understanding of industrial processes, devices, and protocols
* Harness IoT technology to effectively manage industrial use cases
* Design and implement an IIoT network flow to continuously monitor the performance of your critical assets
* Get to grips with popular cloud-based platforms such as AWS and Azure
* Explore Edge devices and learn about Edge and fog computing to gather field data
* Apply diagnostic analytics to real-world data to answer critical workforce questions
* Develop AIoT technology for predictive maintenance

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1835887473) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
Here you can find all the source codes of the chapters of the book _Hands-On Industrial Internet of Things Second Edition_, published by Packt

> :warning: This Book will be available in Q4 2024.

## :books: Chapters from 6 to 15
Chapter 1, Introduction to Industrial IOT, provides some background to the industrial IoT, the story, use cases, and the contrast with the home internet of things. Understanding the Industrial IoT Process 

Chapter 2, Creating Data Flow & Data Sources, Understanding the Industrial Process and Devices, defines the factory processes. This chapter describes the concept of distributed control system (DCS), programmable logic controllers (PLCs), supervisory control and data acquisition (SCADA), Historian, manufacturing execution system (MES), enterprise resources planning (ERP), and fieldbus. It introduces the International Electrotechnical Commission (IEC)-61131 and the CIM pyramid. Finally, it designs a big picture, from equipment through to the cloud. 

Chapter 3, Implementing Data Collection & Industrial IOT Gateway, details which equipment, devices, network protocols, and software layers managing the industrial IoT data flow along its path, from the sensors in the factory floor to the edge that is the external boundary of the industrial IoT data flow inside the factory. 

Chapter 4, Implementing the Industrial IoT Data Flow, explains how to implement the industrial IoT data flow in a complex industrial plant. This journey starts with an understanding of how to select the industrial data source to connect to for the purpose of gathering the data and ends providing five network scenarios for edge deployment in industrial plants. 

Chapter 5, Applying Cybersecurity, explores the industrial IoT data flow from the cybersecurity perspective, outlining the goals of the DiD strategy, and the most common network architecture to secure the industrial control systems, including the five network scenarios for edge deployment discussed in the previous chapter. 

Chapter 6, Performing an Exercise Based on Industrial Protocols and Standards, discovers how to implement a basic data flow from the edge to the cloud by means of OPC UA and Node RED. 

Chapter 7, Developing Industrial IoT and Architecture, outlines the basic concepts regarding industrial IoT data processing, providing the key principles for storing time series data, handling the asset data model, processing the data with analytics, and building digital twins. 

Chapter 8, Implementing On-Premise Industrial IoT platform, shows how to implement a custom platform leveraging on the most popular open source technologies: Node.js, Docker, InfluxDB, Neo4J, Apache Airflow, Mosquitto, and Docker. 

Chapter 9, Building a AWS INDUSTRIAL IOT Solution, explores the solutions proposed by Amazon Web Services (AWS) and the capabilities of the AWS IoT platform. This chapter introduces the Edge IoT of AWS (Greengrass), the IoT Core, AWS SiteWise and build the first part of the proposed architecture. We will learn these technologies by performing a practical exercise. 

Chapter 10, Implementing INDUSTRIAL IOT Data Flow with AWS, concludes the proposed architecture by implementing the Data Flow using DynamoDB, AWS analytics, and Grafana to display data. We will gain practical experience with these technologies through a hands-on exercise. 

Chapter 11, Building a Practical Azure INDUSTRIAL IOT Solution, develops a wing to-wing industrial IoT solution leveraging on Azure, Azure Edge, and the Azure IoT platform. We will learn these technologies by performing a practical exercise. 

Chapter 12, Implementing INDUSTRIAL IOT Data Flow with Azure, finalizes the proposed architecture, implementing the Data Flow with Azure CosmosDB, Stream Analytics and Synapse. We will learn these technologies by performing a practical exercise. 

Chapter 13, Understanding Diagnostics, Maintenance, and Predictive Analytics, introduces the reader to the basic concepts of analytics and data consumption. It also develops basic analytics for anomaly detection and prediction. The chapter also introduces the new concepts of Generative AI. 

Chapter 14, Implementing a Digital Twin , develops a physics-based and data-driven digital equipment model to monitor assets and systems. 

Chapter 15, Deploying Analytics’ Models, shows how to develop analytics on Azure ML and AWS SageMaker. Finally, the chapter explores other common technologies. 


All of the code is organized into folders. For example, Chapter9.

The code will look like the following:
```
if __name__ == '__main__':
  asyncio.run(main())
```

**Following is what you need for this book:**
If you are an IoT architect, developer, AI engineer, or stakeholder involved in designing the architecture systems of the Industrial Internet of Things, this book is for you. The only prerequisite needed is a solid understanding of the Python programming language and networking concepts.

With the following software and hardware list you can run all code files present in the book (Chapter 1-15).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-15 | Python 3.11+ | Windows or Linux |
| 1-15 | Node.js 20+ | Docker or Docker Community Edition |
| 1-15 | Git |  |



### Related products
* Building Secure Automotive IoT Applications [[Packt]](https://www.packtpub.com/en-us/product/building-secure-automotive-iot-applications-9781835462843?utm_source=github&utm_medium=repository&utm_campaign=) [[Amazon]](https://www.amazon.com/dp/1837638039)
* Hands-on ESP32 with Arduino IDE [[Packt]](https://www.packtpub.com/en-us/product/hands-on-esp32-with-arduino-ide-9781837637713) [[Amazon]](https://www.amazon.com/dp/1837638039)

## Get to Know the Authors
**Giacomo Veneri**
was born in Siena, Italy, in 1973. He is an expert in data processing and industrial internet of things (IIoT). Working actively as an AI and IoT manager, he is the author of several books and scientific articles. He graduated from the University of Siena with a degree in computer science in 1999 and graduated in 2014 with a PhD in neuroscience and neural computation. He has achieved more than 10 certifications in programming, AI, and the cloud. Today, Giacomo is an AI director.

**Antonio Capasso**
graduated from the University of Naples with a degree in computer automation in 1999 and a degree in computer science in 2003. He has been working for twenty years on large and complex IT projects related to the industrial world in a variety of fields (automotive, pharma, food and beverage, and oil and gas), in a variety of roles (programmer, analyst, architect, and team leader) with different technologies and software. Since 2011, he has been involved in building and securing IIoT infrastructure. He currently lives in Tuscany, where he enjoys trekking and swimming.

