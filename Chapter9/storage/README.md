# TimeStrean and IOT Analytics/Events

* 📄 json file : source code a json file template for IOT Events

## Query for Timestream

Simple query:
    select device, CPU, Temperature from tsstorage."IoTMulti" order by time DESC 

Interpolate CPU every 2 minutes: 

    SELECT device,  
    BIN(time, 120s) AS binned_timestamp,  
    AVG(CAST(CPU AS double)) AS avg_cpu_utilization 
    FROM tsstorage."IoTMulti"  
    GROUP BY device, BIN(time, 120s) 
    order by binned_timestamp DESC

## Roles for timestream plugin

    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": ["timestream:*"],
        "Resource": "*"
        }
    ]
    }