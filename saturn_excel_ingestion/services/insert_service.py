from mappers.item_mapper import map_row_to_item
from repositories.item_repository import insert_items

def insert_valid_rows(row_results):
    mapped = []
    errors = []

    for sheet in row_results:
        for row in sheet["valid_rows"]:
            try:
                mapped.append(map_row_to_item(row))
            except Exception as e:
                errors.append({
                    "row": row,
                    "error": str(e)
                })

    inserted = 0
    if mapped:
        inserted = insert_items(mapped)

    return {
        "inserted": inserted,
        "mapping_errors": errors
    }
