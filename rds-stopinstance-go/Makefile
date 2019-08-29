.PHONY: deps test clean build deploy

deps:
	go get -u ./...

test: build
	sam local invoke StopRDSInstance -e event.json

clean: 
	rm -rf ./rds-stopinstance
	
build:
	GOOS=linux GOARCH=amd64 go build -o rds-stopinstance

deploy: build
	sam package --output-template-file packaged.yaml --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
	sam deploy --template-file packaged.yaml --stack-name stop-rds-instance --capabilities CAPABILITY_IAM