import sys
import botocore
import boto3
from botocore.exceptions import ClientError
from arnparse import arnparse

def lambda_handler(event, context):
    rds = boto3.client('rds')
    lambdaFunc = boto3.client('lambda')
    print 'Trying to get Environment variable'
    if event['resource_arns']:
        for item in event['resource_arns']:
        	dbitem=arnparse(item)
        	if dbitem.resource_type=='db':
        		DBinstance=str(dbitem.resource)
			    try:
 			        response = rds.stop_db_instance( DBInstanceIdentifier=DBinstance)
        		    print 'Success :: '
                except ClientError as e:
                	print(e)
	else:
		print("No resources found")

	return
    {
        'message' : "Script execution completed. See Cloudwatch logs for complete output"
    }

