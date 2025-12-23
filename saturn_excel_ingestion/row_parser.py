from validators.row_validator import validate_row
from constants import ROW_FIELD_RULES


def parse_rows(workbook, sheet_meta):
    sheet_name = sheet_meta["name"]
    headers = sheet_meta["headers"]

    sheet = workbook[sheet_name]

    valid_rows = []
    invalid_rows = []

    for idx, row in enumerate(
        sheet.iter_rows(min_row=2, values_only=True),
        start=2
    ):
        record = {}

        for col_index, header in enumerate(headers):
            try:
                record[header] = row[col_index]
            except IndexError:
                record[header] = None

        #  ignore completely empty rows
        if all(value in (None, "") for value in record.values()):
            continue

        # Validate row
        is_valid, errors = validate_row(record, ROW_FIELD_RULES)

        if is_valid:
            valid_rows.append(record)
        else:
            invalid_rows.append({
                "row_number": idx,
                "errors": errors,
                "data": record
            })

    return {
        "sheet": sheet_name,
        "total_rows": len(valid_rows) + len(invalid_rows),
        "valid_rows": valid_rows,
        "invalid_rows": invalid_rows
    }
