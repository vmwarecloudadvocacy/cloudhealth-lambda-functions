.PHONY: deps test clean build deploy

deps:
	go get -u ./...

test: build
	sam local invoke EC2Snapshot -e event.json

clean: 
	rm -rf ./ec2-snaphot
	
build:
	GOOS=linux GOARCH=amd64 go build -o ec2-snaphot

deploy: build
	sam package --output-template-file packaged.yaml --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
	sam deploy --template-file packaged.yaml --stack-name ec2-snaphot --capabilities CAPABILITY_IAM