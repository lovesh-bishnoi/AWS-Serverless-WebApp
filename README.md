# AWS-Serverless-WebApp
In this project, I'm building an AWS serverless web application to determine the angle between an analog clock's hour and minute hands using four AWS services: AWS Lambda, API Gateway, AWS Amplify, and DynamoDB. Even though it is a very basic web application, it connects all the essential components that we will use to build a much larger application for the real world.

![image](https://user-images.githubusercontent.com/64860326/212936057-2550705b-e5c5-4fcd-a84d-8d0000194d08.png)

# Working version with example
As shown in the screenshot below, we will enter the appropriate number of hours & minutes and then click the "CALCULATE" button. 

Example: The time at 16:00 (🕓), the angle between the minute and hour hand will be 120 degrees as shown as a result in the pop-up window.
![image](https://user-images.githubusercontent.com/64860326/212993731-d593001a-076f-4761-a2aa-d17f32eb160d.png)

# How should this web application be created?

- How to create/host a website? 
- How to invoke the math functionality? 
- How to perform some math?
- How to store and return the result?

## How to create/host a website? 

**AWS Amplify:** It is used to build and host websites.

### 🔥 Deploy the web application

1. Host the web app using AWS Amplify and select GitHub.
2. Login to the GitHub account. After GitHub authorization, select the repository from the dropdown list (AWS-Serverless-WebApp).
3. Pick the app name and deploy (which basically deploys the index.html).
4. After approx. 2 minutes, the web app will be deployed as shown in the screenshot below.
   ![image](https://user-images.githubusercontent.com/64860326/212956982-e676441b-4a83-4f67-8ff2-c9eed9b5ab61.png)
5. Click on the URL to open the webpage (index.html) ✅ 
   ![image](https://user-images.githubusercontent.com/64860326/212993464-f885511c-cd53-4719-982d-2c10f36c3d9d.png)

## How to perform some math?

**AWS Lambda:** It is serverless and runs the code upon the trigger. 

### 🔥 Deploy the Lambda function

1. Create the lambda function with the name "ClockAngle-Lambda" and select the language "Python 3.9"
2. Go to "Code source" and copy the code from the "lambda.py" file and replace the whole code in "Code source".
3. Click on "Deploy".

### 🔥 Test the Lambda function

4. Test the code by configuring the test event from the Test dropdown button.
5. Create a new event with the name "Lambda-test" and write the code in Event JSON as shown below (example) and click on save.
      ```
      {
        "hours": 17,
        "mins": 0
      }
      ```
6. Click on the Test button to test the Lambda_function.py with the value mentioned in the "Lambda-test" event.
7. For input time 17:00 (🕔), the result is 150 degrees as shown in the screenshot ✅ (i.e. Lambda function is working perfectly 💪)
   ![image](https://user-images.githubusercontent.com/64860326/212963663-de8a08f6-036f-40d5-8f68-229b7176373a.png)

## - How to invoke the math functionality (Lambda function)? 

**API Gateway:** It is used to build HTTP, REST, and WebSocket APIs

###  🔥 Deploy the API Gateway

1. Create a new Rest API (public) and name it "ClockAngle-API".
2. Create a method from the "Actions" dropdown, select "POST" from the dropdown shown in the screenshot below, and click on ✅ next to it.
   ![image](https://user-images.githubusercontent.com/64860326/212967449-0cd8dc44-01cc-46f2-a8d4-2665d7d9e0d2.png)
3. Select the lambda function which we created "ClockAngle-Lambda" and click on the save button.
4. Select POST and enable CORS from the "Actions" dropdown and click on "Yes, replace existing values". 
    - As Amplify is in one domain and the lambda function is in another domain. So, in order to call the lambda function from the web application running on Amplify, we need to enable CORS which is Cross-Origin Resource Sharing.
5. Deploy API from the "Actions" dropdown. Choose the Deployment stage as [New Stage] and Stage name as "dev" and click on Deploy.
6. Copy the Invoke URL and save it somewhere for later use.

###  🔥 Test the API Gateway

7. Click on "Resources" and select "POST". On the right side, we can see POST - Method Execution which shows how API is going to make the method request to the lambda function, and in response, Lambda is going to send the Method response to API Gateway (as shown below).
   ![image](https://user-images.githubusercontent.com/64860326/212972448-5ab0a9ac-3283-4a5c-84b6-ac2768940b1c.png)
8. To test the API gateway, click on lightening bolt 🌩️ and write the below code in "Request Body" as
      ```
      {
          "hours": 9,
          "mins": 30
      }
      ```
9. The result is 105 degrees for 9:30 am (🕤) as shown in the screenshot ✅ (i.e. API Gateway is working perfectly with Lambda function 💪)
   ![image](https://user-images.githubusercontent.com/64860326/212973818-f362e455-211d-40a3-b8d8-6492858ea135.png)

## - How to store and return the result?

**DynamoDB:** It is a serverless key-value (NoSQL) lightweight database (best for this scenario). However, the result can be displayed on the webpage only but I wanted to provision the backend and store/return the value from the database.

###  🔥 Create a table in DynamoDB

1. Create a new table as "ClockAngle-DynamoDB" with the Partition key as "ID".
2. Copy the ARN by selecting the table --> Overview --> General information and save it somewhere for later use.

###  🔥 Provide permission to the lambda function to store the result in the DynamoDB table

3. Go to Lambda function: Go to Configuration --> Permissions --> Execution role --> Click on the role name --> In the new window, create an inline policy from Add permissions.
4. Click on the JSON tab and replace the code with the below code and paste the saved ARN of the DynamoDB table to the resource section by replacing "YOUR-TABLE-ARN" in the code. Alternatively, the permissions can be manually assigned using the visual editor.
      ```
      {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "VisualEditor0",
              "Effect": "Allow",
              "Action": [
                  "dynamodb:PutItem",
                  "dynamodb:DeleteItem",
                  "dynamodb:GetItem",
                  "dynamodb:Scan",
                  "dynamodb:Query",
                  "dynamodb:UpdateItem"
              ],
              "Resource": "YOUR-TABLE-ARN"
          }
          ]
      }}
      ```
5. Click on the Review and create the policy with the name "ClockAngle-LambdaPolicy".
6. Update the lambda_function by removing all 4 triple single quotes (""") (highlighted green) in the code or replacing the whole code with the "Lambda-            final.py".
7. Click on Deploy and Test the code with either a new test event (refer Test section in Lambda function) or with the existing saved event "Lambda-test".
8. With the "Lambda-test" event, the result is 150 degrees and will be stored in the DynamoDB table shown below. ✅ (i.e. Lambda function is working perfectly with DynamoDB table 💪)
   ![image](https://user-images.githubusercontent.com/64860326/212983331-0468314d-0204-451b-bdc1-c25d7634b84f.png)

###  🔥 Final step as the connector is missing between Amplify and API Gateway
9. Paste & replace the saved API Gateway URL with "YOUR API GATEWAY ENDPOINT" in the index.html file. Commit the changes to the index.html file and Push the project.
10. AWS Amplify will automatically deploy the web application as soon as changes are made.

# Let's run the web application

  For example: Time at 18:00 🕕 and the angle between the hour hand and the minute hand is 180 degrees. Let's check it with the web application, also whether the result is saved in the DynamoDB table or not.
  **Result**: 180 degrees ✅💪😊
  ![image](https://user-images.githubusercontent.com/64860326/212993902-1adc7d8c-9227-4521-a4cc-b745e71c6e06.png)
  The result is saved in DynamoDB ✅💪😊
  ![image](https://user-images.githubusercontent.com/64860326/212994409-8b144341-5570-431d-9248-cc49c55bac2e.png)
