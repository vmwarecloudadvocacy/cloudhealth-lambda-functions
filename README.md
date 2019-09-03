# CloudHealth Lambda Functions

Serverless apps are very efficient at running code, so what if we leveraged [AWS Lambda](https://aws.amazon.com/lambda/) to automate [governance policies](https://www.cloudhealthtech.com/solutions/centralize-cloud-governance) for multi-cloud environments? This repository has several AWS Lambda functions that can be triggered from [CloudHealth](https://www.cloudhealthtech.com/).

## Get Started

There are a few steps to get started with the AWS Lambda samples in this repository.

* [Install SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Install Docker](https://docs.docker.com/install/) if you want to test the apps on your local machine.

## Current apps

* Stop RDS instances - Stops RDS instances (looks for ARN values from CloudHealth with `resource type='db'`)
* Snapshot EC2 instances - Takes a snaphot of an EC2 instance (looks for ARN values from CloudHealth with `resource type = 'instance'`)
* Modify EBS volume - Updates the size of an EBS volume (looks for ARN values from CloudHealth with `resource type = 'instance'`)

All samples are available in Python and Go

## Contributing

If you have any thoughts on which functions we could add, feel free to raise a [new issue](https://github.com/vmwarecloudadvocacy/cloudhealth-lambda-functions/issues/new). If you want to contribute your own functions to this repository, feel free to open a [Pull Request](https://github.com/vmwarecloudadvocacy/cloudhealth-lambda-functions/compare).

## License

All of these functions are available under the [MIT license](./LICENSE).
