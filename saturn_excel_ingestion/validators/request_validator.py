import json
from constants import REQUIRED_FIELDS

def validate_request(event):
    body = event.get("body")
    if not body:
        return _invalid("Request body is required")

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return _invalid("Invalid JSON format")

    missing_fields = [
        field for field in REQUIRED_FIELDS
        if field not in data or not data[field]
    ]

    if missing_fields:
        return _invalid(
            "Missing required fields",
            missing_fields
        )

    if data.get("file_type") != "excel":
        return _invalid("file_type must be 'excel'")

    return {
        "valid": True,
        "data": data
    }

def _invalid(error, details=None):
    return {
        "valid": False,
        "error": error,
        "details": details
    }
