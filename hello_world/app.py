import json

# import requests


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "AWSLambda_FullAccess removed!",
            # "location": ip.text.replace("\n", "")
        }),
    }
