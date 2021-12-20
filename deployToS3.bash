#!/bin/bash

sftp -i "/Users/briankim/Documents/aws_instance/key2.pem" ec2-user@ec2-18-219-129-246.us-east-2.compute.amazonaws.com  <<EOF


put lambda_function.py lambda_function/
put ynab.py lambda_function/
put rhAPI.py lambda_function/
put gmail.py lambda_function/
put modifyWord.py lambda_function/
put config.py lambda_function/
put ynabTemplate.docx lambda_function/

EOF


