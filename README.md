# Inbox: Automated Accountant

## Description
Automated python script that builds and sends my personalized monthly financial report to my inbox. 


### 5 Components
1) Consume **You Need a Budget (YNAB) + Robinhood(RH) API** to gather necessary financial data
2) Analyze my financial data to build new data and format them in a Microsoft Word Document using **docxtpl module**
3) Attach financial report to email and send it to my inbox using **smtplib + email module**
4) Automate



Passive Focus:
1) Modularity
2) Clean Code
3) OOP
4) Unit Testing
5) Well Documented



## Motivation
1) This project is the first quest to automate my personal life. It saves me about an hour every month.
2) After a year of not being able to code, I want test and improve my skills as a software developer. 


Lambda Function:
Resources:
**Lambda Intro: **https://www.youtube.com/watch?v=seaBeltaKhw&ab_channel=StephaneMaarek

**Lambda Functionalities: **https://www.youtube.com/watch?v=K-nnzpgrzwM&ab_channel=BeABetterDev

**Import Open Source Module: ** https://www.youtube.com/watch?v=yyBSeGkuPqk&ab_channel=Cairocoders

*** Scheduling Lambda *** https://www.youtube.com/watch?v=rDbxCeTzw_k&ab_channel=PyLenin


## AWS Lambda + EC2 Instance
1) To automate, I am trying to run python script on AWS Lambda. Note all dependencies must be accessed by the handler (Eithier have dependencies in the same directory or import them using path in handler file)

### Issue 1: Incorrect dependencies (lxml) based on the operating system (OS (mine) vs Linux (AWS))
### Solution: Build all depenencies in AWS EC2 Instance + Send update lambdaFunction
2) Transfer lambdaFile in local directory to aws ec2 instance (sftp)
3) (ec2 instance) Activate venv. Install all depdencies into target folder. Otherwise some dependencies will be split between lib, lib36, lib64 files. We want them all in one file so we can easily zip
pip install --target=./venv/lib/python3.7/site-packages -r requirements.txt 
4) zip all modules necessary to deploy lambda function
cd venv/lib/python3.7/site-packages/
zip -r ../../../../ deployment.zip .
cd ../../../../
zip -g deployment.zip config.py modifyWord.py gmail.py rhAPI.py ynab.py ynabTemplate.docx lambda_function.py
gip -g deployment.zip statements/
5) Update lambdaFunction
aws lambda update-function-code --function-name inbox --zip-file deployment.zip

