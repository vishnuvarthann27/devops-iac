import json
import boto3

def lambda_handler(event, contect):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    tableBooks = dynamodb.Table('Books')
    body = json.loads(event['body'])


    id = body['id']
    title = body['title']
    author = body['author']

    try:
        tableBooks.put_item( Item = {'id':str(id), 'title': title, "author" : author})
        return {
            'statusCode' : 200,
            'body' : json.dumps('Successfully created record')
        }
    except Exception as ex:
        print(ex)
        return {
            'statusCode' : 400,
            'body' : json.dumps('Error creating record')
        }