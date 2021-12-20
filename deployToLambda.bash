#!/bin/bash

#VARIABLES: AWS S3 Instance (Public DNS)

#NOTE: Dependencies were previously created in s3 instance. Transfered back to local machine.
#      Then made some edits to robin_stocks/robinhood/authentication.py. Therefore prepackaged dependencies


#Open S3 instance. Recreate lambda_function folder
#SFTP all necessary files to instance (including dependencies)
#Send to AWS Lambda

#Log into S3 Instance. Delete existing folder and create new empty folder "lambda_function"
ssh -i "/Users/briankim/Documents/aws_instance/key2.pem" ec2-user@ec2-18-219-129-246.us-east-2.compute.amazonaws.com <<EOF
rm -r lambda_function
mkdir lambda_function

EOF

#Send all files and dependencies.zip to S3 Instance.
sftp -i "/Users/briankim/Documents/aws_instance/key2.pem" ec2-user@ec2-18-219-129-246.us-east-2.compute.amazonaws.com  <<EOF


put lambda_function.py lambda_function/
put ynab.py lambda_function/
put rhAPI.py lambda_function/
put gmail.py lambda_function/
put modifyWord.py lambda_function/
put config.py lambda_function/
put ynabTemplate.docx lambda_function/
put deployToLambda.bash lambda_function/
#only has dependencies right now
put dependencies.zip lambda_function

EOF

#Zip all the files together
#Send it to AWS Lambda
ssh -i "/Users/briankim/Documents/aws_instance/key2.pem" ec2-user@ec2-18-219-129-246.us-east-2.compute.amazonaws.com <<EOF
cd lambda_function

# mkdir deployment
# pip3 install --target=./deployment robin_stocks
# pip3 install --target=./deployment pyotp
# pip3 install --target=./deployment docxtpl

unzip dependencies
cd dependencies
zip -r ../deployment.zip .
cd ../
zip -g deployment.zip config.py modifyWord.py gmail.py rhAPI.py ynab.py ynabTemplate.docx lambda_function.py


aws lambda update-function-code --function-name automate_document --zip-file fileb://deployment.zip
EOF

