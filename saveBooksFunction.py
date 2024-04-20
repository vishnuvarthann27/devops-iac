import json
import boto3

def lambda_handler(event, contect):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    tableBooks = dynamodb.Table('Books')

    id = event['id']
    title = event['title']
    author = event['author']

    try:
        tableBooks.put_item( Item = {'id':id, 'title': title, "author" : author})
        return {
            'statusCode' : 200,
            'body' : json.dumps('Successfully created record')
        }
    except:
        return {
            'statusCode' : 400,
            'body' : json.dumps('Error creating record')
        }