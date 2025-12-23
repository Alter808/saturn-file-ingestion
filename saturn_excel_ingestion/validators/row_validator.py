def validate_row(row: dict, rules: dict):
    errors = []

    for field, rule in rules.items():
        value = row.get(field)

        # null allowed
        if value in (None, ""):
            if not rule.get("nullable", True):
                errors.append(f"{field} is required")
            continue

        expected_type = rule.get("type")

        if expected_type == "number":
            if not isinstance(value, (int, float)):
                errors.append(f"{field} must be numeric")

        elif expected_type == "string":
            # any non-null value is valid
            pass

    return len(errors) == 0, errors
