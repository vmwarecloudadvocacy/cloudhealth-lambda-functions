# Cloudhealth lambda functions 

This repository stores lambda functions that can be triggered from CH. They look for a specific input which is
sent in from CloudHealth. That input is parsed for specific values which are used to trigger different actions.
Examples:

* Stop RDS instances - looks for ARN values from CH with resource type='db'
* Snapshot EC2 instances - looks for ARN values from CH with resource type = 'instance'

The code is all written in python with the specific dependencies

* ARNparse library
* boto3 library
* uses python3

The function.zip files are built to be directly loaded into AWS with the following command:
```
aws --region ca-central-1 lambda update-function-code --function-name snapshotec2 --zip-file fileb://function.zip
```

If you make changes please rebuild the function.zip with the following command:
```
zip -r9 function.zip .
```

Happy trails ;-)

