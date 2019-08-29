# rds-stopinstance-go

This app stops RDS instances (by looking for ARN values from CloudHealth with `resource type='db'`)

```bash
.
├── event.json       <-- Sample event data from CloudHealth
├── go.mod           <-- Go module file
├── go.sum           <-- Cryptographic hash of used Go modules
├── main.go          <-- Lambda function code
├── Makefile         <-- Make to automate build
├── README.md        <-- This instructions file
└── template.yaml    <-- SAM deployment file
```

## Make targets

| Target | Description                                           |
|--------|-------------------------------------------------------|
| deps   | Get the dependencies (Go modules) the app depends on  |
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
