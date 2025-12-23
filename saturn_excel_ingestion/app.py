import json
from multipart_parser import parse_multipart
from validators.request_validator import validate_request
from responses import ok, bad_request
from services.excel_service import save_excel_to_tmp, analyze_excel, process_valid_sheets
from constants import REQUIRED_SHEET_COLUMNS, ENABLE_ROW_VALIDATION
from services.insert_service import insert_valid_rows

def lambda_handler(event, context):
    # parse multipart/form-data
    try:
        fields, files = parse_multipart(event)
    except Exception as e:
        return bad_request(str(e))

    # validate metadata (source, uploaded_by, file_type)
    result = validate_request({
        "body": json.dumps(fields)
    })

    if not result["valid"]:
        return bad_request(result["error"], result.get("details"))

    if "file" not in files:
        return bad_request("Missing file field")

    file_info = files["file"]
    file_bytes = file_info["content"]
    filename = file_info["filename"] or "upload.xlsx"

    # 1) save to /tmp
    tmp_path = save_excel_to_tmp(file_bytes, filename)

    # 2) analyze excel file
    try:
        info = analyze_excel(
            tmp_path,
            rules={
                "required_columns": REQUIRED_SHEET_COLUMNS
            }
        )
        # 3) process valid sheets with row validation only if enabled
        if ENABLE_ROW_VALIDATION:
            row_results = process_valid_sheets(tmp_path, info)
            insert_result = insert_valid_rows(row_results)
        else:
            row_results = []
    except Exception as e:
        return bad_request("Failed to read Excel file", str(e))

    return ok(
    "Excel processed and inserted",
    {
        "sheets": info,
        "rows_summary": [
            {
                "sheet": s["sheet"],
                "valid": len(s["valid_rows"]),
                "invalid": len(s["invalid_rows"])
            } for s in row_results
        ],
        "db": insert_result
    }
)

