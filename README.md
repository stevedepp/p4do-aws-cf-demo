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

|Imperative             |Declarative                    |
|--:                    |--:                            |           
|procedural orientation | object orientation            | 
|coded steps		 		    | classes of objects that exist |
							cloud service provider for procedures

Project 4

DynamoDB —> EventBridge —> Lambda —>                  SQS —>         Lambda —>     AWS comprehend —> S3
fang —>             5minutetimer —> serverlessproducer —> producer —> producerai —> comprehend —>            fangsentiment-depp


<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/113652952-d3d75c80-9662-11eb-834d-3880404101a2.png">



