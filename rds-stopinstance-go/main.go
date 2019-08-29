package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/rds"
)

func handler(request map[string]interface{}) error {
	// Get the ARNs from the CloudHealth message
	events := request["resource_arns"].([]interface{})

	// Create a new session without AWS credentials.
	// This means the Lambda function must have privileges to access RDS
	awsSession := session.Must(session.NewSession(&aws.Config{
		Region: aws.String(os.Getenv("REGION")),
	}))

	// Create a client to the RDS service
	rdsClient := rds.New(awsSession)

	// Loop over the ARNs and if they are databases, try to stop the RDS instance
	for _, event := range events {
		arn := event.(string)
		elem := strings.Split(arn, ":")
		if strings.Contains(arn, ":db:") {
			stopRequest := &rds.StopDBInstanceInput{
				DBInstanceIdentifier: aws.String(elem[6]),
			}
			stopResponse, err := rdsClient.StopDBInstance(stopRequest)
			if err != nil {
				fmt.Printf("error occurred while trying to stop %s: %s\n", elem, err.Error())
				continue
			}
			fmt.Printf("current status for %s: %s\n", elem, *stopResponse.DBInstance.DBInstanceStatus)
		}
	}

	return nil
}

func main() {
	lambda.Start(handler)
}
