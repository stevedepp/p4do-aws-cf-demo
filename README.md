## MSDS 498 final project demo video for week 6: *Quick update*

Serverless AI Data Engineering Pipeline via: 
- [x] AWS consoles 
- [x] AWS CLI 
- [x] AWS SDK (Boto)
- [x] AWS Serverless Application Model
- [ ] AWS CloudFormation

Please click the video to hear sound or follow along with the transcript that's set just below the video.

![demo](https://user-images.githubusercontent.com/38410965/111997815-cd3cd700-8af1-11eb-96fb-467bb5673f18.mp4)

#

> Hello everyone. Thank you for watching. This video is less a demo and more an update. I have been working on project 4 which builds a serverless ai data engineering pipeline. 3 weeks ago, I completed the building of this project infrastruture
using the AWS service consoles to create 6 objects: a dynamoDB table called 'fang', shown here on the left in the middle of the page; an eventbridge event, named '5 minute timer', that triggers a lambda function, called 'serverlessproducer', that gets from 'fang' and gives to a simple queue service; a second lambda function, called 'producerai', that is triggered by SQS entries and gives to AWS comprehend to process, and finally over to S3 for retrieval. 

**Demo Video 6**

### Serverless AI Data Engineering Pipeline
### Quick update

**Steve Depp**
**MSDS 498 section 61**

**Objective:**  Build infrastructure 
- [x] AWS service consoles
￼
<img width="303" alt="AWS services" src="https://user-images.githubusercontent.com/38410965/113652820-88bd4980-9662-11eb-9232-e86211f3d0f7.png">

**Project 4**

**DynamoDB —> EventBridge —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**   
fang —> 5minutetimer —> serverlessproducer —> producer —> producerai —> comprehend —>            fangsentiment-depp
￼

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/113652834-8f4bc100-9662-11eb-956d-16443161eaf7.png">

#

> With that, I've learned how to build infra in a service providers web interface. It is easy, and not intimidating, but it's slow. It leaves you at the mercy of someones GUI, and has no leverage with respect to time or people: If you want another one of these, you need to pull up these web interfaces each time and at my quickest, it took 24 minutes.  So,
last week into part of this week, ...
 
**Demo Video 6**

### Serverless AI Data Engineering Pipeline
### Quick update

**Steve Depp**
**MSDS 498 section 61**

**Objective:** Infrastructure via **web interface**   
- [x] AWS service consoles
    - [x] DynamoDB
    - [x] SQS
    - [x] Lambda
    - [x] IAM
    - [x] EventBridge
    - [x] S3

	**—> AWS familiarity** 

	**—>	Dependence on GUI = no leverage wrt time / people / code**

**Project 4**

**DynamoDB —> EventBridge —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**   
fang —> 5minutetimer —> serverlessproducer —> producer —> producerai —> comprehend —>            fangsentiment-depp

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/113652888-b1ddda00-9662-11eb-8ea0-6cc370a9e931.png">

#

> ... I implemented the same via a combination of AWS command line interface, AWS SDK for python, aka 'boto3', and AWS serverless application model.  I was pretty happy that I could learn proficiency in these environments in a week, but I hit a hiccup in getting one of my lambdas some visibility.  This hiccup reveals a weakness of this form of IAC. In this form of IAC, I am dependent on the procedural nature of python.  In other words, I gain leverage via code and so my building takes 3 minutes not 24, but to get it done I must tell my 5 minute timer to look at serverless producer and serverless producer to see 5 minute timer.

### Serverless AI Data Engineering Pipeline
### Quick update

**Steve Depp**
**MSDS 498 section 61**

**Objective:** Infrastructure as **code** 
- [x] AWS service consoles
    - [x] DynamoDB
    - [x] SQS
    - [x] Lambda
    - [x] IAM
    - [x] EventBridge
    - [x] S3
- [x] AWS Command Line Interface aka AWS CLI
- [x] AWS SDK for Python aka Boto
- [x] AWS Serverless application model aka AWS SAM

**—> Infrastructure detailed relationships / logic**

**—>	weakness: python as procedural language**


**Project 4**

**DynamoDB —> EventBridge —> Lambda —>                  SQS —>         Lambda —>     AWS comprehend —> S3**   
fang —>             5minutetimer —> serverlessproducer —> producer —> producerai —> comprehend —>            fangsentiment-depp

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/113652919-c15d2300-9662-11eb-99be-4de8bb944d2d.png">

#

> This  brings us to this week where I've been working with CloudFormation which transitions from python’s procedural orieintation to more of an object orientation. In some ways, this is a shift from imperative programming to declarative programming: I state via templates what objects object attributes and object methods I want, and I leave it to the cloud service provider to hook everything up.  The good thing is this will improve my productivity.  It may still take 3 minutes to build the infrastructure, but less time to write the code that does that.  This frees me up to create a command line tool and an API to interface the user.  So my focus shifts from the solution to the customer.  It still leaves me vulnerable to the cloud service provider for procedural implementation, but that provides me significant leverage with respect to time and code, and because its a form of abstraction, I might be more capable of shifting from AWS to GCP and Azure.  So, this time next week, I will have cloud formation done and hoping to spend the remaining weeks on encryption, IAM role tightening, and other aspects of the project.  Thank you very much for watching. 

### Serverless AI Data Engineering Pipeline
### Quick update

**Steve Depp**
**MSDS 498 section 61**

**Objective:** Infrastructure as **templates**   
- [x] AWS service consoles
- [x] AWS Command Line Interface aka AWS CLI
- [x] AWS SDK for Python aka Boto
- [x] AWS Serverless application model aka AWS SAM
- [ ] AWS CloudFormation
- [ ] command line tool: click & flask
- [ ] GCP

|Imperative             |Declarative                          |
|--:                    |--:                                  |           
|procedural orientation |object orientation                   | 
|coded steps            |classes of objects that exist        |
|                       |cloud service provider for procedures|

**Project 4**

**DynamoDB —> EventBridge —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**   
fang —> 5minutetimer —> serverlessproducer —> producer —> producerai —> comprehend —>            fangsentiment-depp

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/113652952-d3d75c80-9662-11eb-834d-3880404101a2.png">

