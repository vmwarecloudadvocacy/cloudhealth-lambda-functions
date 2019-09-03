.PHONY: deps test clean build deploy

deps:
	pip install -r requirements.txt

test: build
	sam local invoke EC2Snapshot -e event.json

clean: 
	rm -rf ./aws-sam
	
build:
	sam build

deploy: build
	sam package --output-template-file packaged.yaml --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
	sam deploy --template-file packaged.yaml --stack-name ec2-snaphot --capabilities CAPABILITY_IAM