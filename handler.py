import json

def throw_error(event, context):
    data = json.loads(event['body'])
    print(data) # this can be seen in CloudWatch Logs

    response = {
        "statusCode": 400,
        "headers": {
            "Content-Type": 'application/json',
            "context.aws_request_id": context.aws_request_id # for fun show the Lambda requestID
        },
        "body": "Bad Request",
        "isBase64Encoded": False
    }

    return response

