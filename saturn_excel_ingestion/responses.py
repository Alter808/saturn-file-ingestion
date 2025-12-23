import json

def ok(message, data=None):
    body = {"message": message}
    if data is not None:
        body["data"] = data
    return _response(200, body)

def bad_request(error, details=None):
    body = {"error": error}
    if details is not None:
        body["details"] = details
    return _response(400, body)

def _response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }
