# Inbox: Automated Accountant

## Description
Identified a need to increase efficiency in tracking financial health. Created an automated solution to visualize and track finances. Results of solution delivered via email to allow for a timely notification and increased productivity



## Design
<p align="center">
  <img src="process.JPG" width="550" title="hover text">
 
</p>

## Report Template
<p align="center">
  <img src="reportExample.JPEG" width="550" title="hover text">
</p>


### 5 Components
1) Consume **You Need a Budget (YNAB) + Robinhood(RH) API** to gather necessary financial data
2) Analyze my financial data to build new data and format them in a Microsoft Word Document using **docxtpl module**
3) Attach financial report to email and send it to my inbox using **smtplib + email module**
4) Automate python Script -> AWS Lambda Function + Trigger using EventBridge (CloudWatch Events) and API Gateway



Passive Focus:
1) Modularity
2) Clean Code
3) OOP
5) Well Documented



### Transitioning from Python Script -> Lambda Function
Install modules/lib/dependencies not provided by AWS Lambda to the same directory 

Issue:  **lxml **  lib not compatibly in lambda (linux) vs local (mac os x)
Solution: sftp code to AWS EC2 Instance. download dependencies in EC2 environment (linux). Downloaded dependencies back to local computer (dependencies.zip)

Notes: Changed **"statement" file to "tmp"**. Lambda only allows you to write into /tmp directory

Issue: robin_stocks/robinhood/authentication.py creates pickle file in home directory. Causes error because Lambda only allows yo to write to /tmp directory
Solution: **Edit authentication.py file ** to not write into home directory


Created a batch file that automatically sends deployment.zip to AWS Lambda from project directory. Remember to ** change Public DNS ** whenever I change instance.
Future To DO:
- Create instance from terminal

Additional Resources: 
**Lambda Intro: **https://www.youtube.com/watch?v=seaBeltaKhw&ab_channel=StephaneMaarek

**Lambda Functionalities: **https://www.youtube.com/watch?v=K-nnzpgrzwM&ab_channel=BeABetterDev

**Import Open Source Module: ** https://www.youtube.com/watch?v=yyBSeGkuPqk&ab_channel=Cairocoders

*** Scheduling Lambda *** https://www.youtube.com/watch?v=rDbxCeTzw_k&ab_channel=PyLenin


## Motivation
1) This project is the first quest to automate my personal life. It saves me about 2-3 hours every month.
2) After a year of not being able to code, I want test and improve my skills as a software developer. 








### Notes: Cannot used some depedencies (lxml) installed locally (OS) on AWS Lambda (Linux). Therefore build all dependencies in AWS EC2 Instance -> send zip


