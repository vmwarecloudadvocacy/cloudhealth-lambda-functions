import sys
import botocore
import boto3
import os
from botocore.exceptions import ClientError
from arnparse import arnparse

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name=os.getenv('REGION', 'us-west-2'))
    client= boto3.client('ec2')
    lambdaFunc = boto3.client('lambda')
    print('Trying to get Environment variable')
    if event['resource_arns']:
        for item in event['resource_arns']:
            citem=arnparse(item)
            if citem.resource_type=='instance':
                ec2instance=str(citem.resource)
                try:
                    volumes=client.describe_instance_attribute(InstanceId=ec2instance, Attribute='blockDeviceMapping')
                    VolumeId=volumes['BlockDeviceMappings'][1]['Ebs']['VolumeId']
                    response = client.modify_volume(VolumeId='VolumeId',VolumeType='sc1',Size=500)
                    print('Success :: conversion', ec2instance)
                except ClientError as e:
                    print(e)
    else:
        print("No resources found")

    return { 'message' : "Script execution completed. See Cloudwatch logs for complete output" }

