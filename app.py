import time


def handler(event, _):
    time.sleep(event.get("sleep", 1))
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
        },
        "body": "",
        "isBase64Encoded": False,
    }
