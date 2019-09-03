# ebs-modify-volume-python

This app updates the size of an EBS volume (looks for ARN values from CloudHealth with `resource type = 'instance'`)

```bash
.
├── app.py           <-- Lambda function code
├── event.json       <-- Sample event data from CloudHealth
├── Makefile         <-- Make to automate build
├── README.md        <-- This instructions file
├── requirements.txt <-- The requirements, installable with pip
└── template.yaml    <-- SAM deployment file
```

## Make targets

| Target | Description                                           |
|--------|-------------------------------------------------------|
| deps   | Get the dependencies the app depends on               |
| test   | Run the Lambda app locally, using docker              |
| clean  | Removes previous executables                          |
| build  | Create a new executable                               |
| deploy | Deploy the app to AWS Lambda (see more details below) |

## Deployment

Deployments to AWS Lambda, using SAM, are done by uploading the code to an `S3 bucket`. If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
aws s3 mb s3://BUCKET_NAME
```

In the [Makefile](./Makefile), you'll need to replace `REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME` with the name of your S3 bucket. After that, `make deploy` will build and deploy the app for you.
