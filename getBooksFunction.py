import json
import boto3

def lambda_handler(event, contect):
    dynamodb = boto3.resource('dynamodb')

    tableBooks = dynamodb.Table('Books')
    response = tableBooks.scan()
    print(response)
    return {
        'statusCode' : 200,
        'body' : response['Items']
    }
