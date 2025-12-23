from typing import Dict, List, Set

# Normalizes header by stripping whitespace and converting to lowercase
def normalize_header(value):
    if value is None:
        return None
    return str(value).strip().lower()

# Validates sheets in the workbook against the provided rules
def validate_sheets(workbook, rules: Dict) -> Dict:
    required_columns: Set[str] = {
        col.lower() for col in rules.get("required_columns", [])
    }

    valid_sheets: List[Dict] = []
    invalid_sheets: Dict[str, str] = {}

    for sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]

        # Read header row
        header_row = next(
            sheet.iter_rows(min_row=1, max_row=1, values_only=True),
            None
        )

        if not header_row:
            invalid_sheets[sheet_name] = "Header row missing"
            continue

        headers = [
            normalize_header(h)
            for h in header_row
            if normalize_header(h)
        ]

        if not headers:
            invalid_sheets[sheet_name] = "Header row is empty"
            continue

        header_set = set(headers)
        missing = required_columns - header_set

        if missing:
            invalid_sheets[sheet_name] = (
                f"Missing required columns: {', '.join(sorted(missing))}"
            )
            continue

        # Sheet is valid
        valid_sheets.append({
            "name": sheet_name,
            "headers": headers
        })

    return {
        "valid_sheets": valid_sheets,
        "invalid_sheets": invalid_sheets
    }
