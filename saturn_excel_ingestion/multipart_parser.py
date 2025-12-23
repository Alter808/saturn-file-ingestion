import base64
from requests_toolbelt.multipart import decoder

def parse_multipart(event):
    # Extract Content-Type header
    headers = event.get("headers") or {}
    content_type = headers.get("Content-Type") or headers.get("content-type")

    # Validate presence of Content-Type
    if not content_type:
        raise ValueError("Missing Content-Type header")

    # Extract body
    body = event.get("body")
    if body is None: # Empty body
        raise ValueError("Empty request body")

    # Decode body
    if event.get("isBase64Encoded", False):
        body_bytes = base64.b64decode(body)
    else:
        body_bytes = body.encode("latin-1")

    # Parse multipart data
    multipart_data = decoder.MultipartDecoder(body_bytes, content_type)

    fields = {}
    files = {}

    # Process each part
    for part in multipart_data.parts:
        disposition = part.headers.get(b"Content-Disposition", b"").decode()

        if "filename=" in disposition:
            # It's a file part
            name = disposition.split('name="')[1].split('"')[0]
            filename = disposition.split('filename="')[1].split('"')[0]

            files[name] = {
                "filename": filename,
                "content_type": part.headers.get(b"Content-Type", b"").decode(),
                "content": part.content
            }
        else:
            name = disposition.split('name="')[1].split('"')[0]
            fields[name] = part.text

    return fields, files
