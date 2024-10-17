import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('sagemaker-runtime')
    wind_speed_ms = event["wind_speed_ms"]

    CONTENT_TYPE = 'text/csv'
    endpoint_name="windturbine"

    encoded_text = f"{wind_speed_ms}"

    response = client.invoke_endpoint(EndpointName=endpoint_name, 
                                  ContentType=CONTENT_TYPE, 
                                  Body=encoded_text)

    response_payload = json.loads(response['Body'].read().decode("utf-8"))

    print(response_payload)
    return response_payload