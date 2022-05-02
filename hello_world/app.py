import json

# import requests


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "AmazonS3OutpostFullAccess, AWSCloudFormationReadOnlyAccess removed!",
            # "location": ip.text.replace("\n", "")
        }),
    }
