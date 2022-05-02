import json

# import requests


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": " all 3 required ones",
            # "location": ip.text.replace("\n", "")
        }),
    }
