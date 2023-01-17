# import the JSON utility package
import json

"""
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('ClockAngles-DynamoDB')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
"""

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    # extract the two numbers from the Lambda service's event object
    hours = int(event.get('hours'))
    while hours > 23:
        hours = int(event.get('hours'))
    mins = int(event.get('mins'))
    while mins > 59:

        mins = int(event.get('mins'))

    if hours > 12:
        hours = hours - 12
    angle_mins = mins * 6
    angle_hours = hours * 30 + (0.5 * mins)
    angle_btw_hands = abs(angle_hours - angle_mins)
    if angle_btw_hands > 180:
        angle_btw_hands = 360 - angle_btw_hands

    """
    # write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': str(angle_btw_hands),
            'LatestGreetingTime': now
        })
    """

    # return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('The angle between clocks hands is ' + str(angle_btw_hands))
    }
