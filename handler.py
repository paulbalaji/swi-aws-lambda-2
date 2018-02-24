import json
import datetime

def tracker(event, context):
    
    body = {
        "message": "test post pls ignore"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
