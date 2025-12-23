def map_row_to_item(row: dict):
    """
    Normalize and cast values before DB insertion. 
    Throw a ValueError if conversion fails for critical data
    """
    def to_int(v):
        if v in (None, ""):
            return None
        return int(v)

    def to_str(v):
        if v in (None, ""):
            return None
        return str(v).strip()

    return {
        "admin_name": to_str(row.get("admin_name")),
        "admin_form_name": to_str(row.get("admin_form_name")),
        "admin_pretest_form_name": to_str(row.get("admin_pretest_form_name")),
        "admin_session_id": to_int(row.get("admin_session_id")),
        "admin_base_session_item_num": to_str(row.get("admin_base_session_item_num")),
        "admin_scram_session_item_num": to_str(row.get("admin_scram_session_item_num")),
        "set_id": to_str(row.get("set_id")),
        "set_name": to_str(row.get("set_name")),
        "item_id": to_str(row.get("item_id")),
        "item_id_itest": to_str(row.get("item_id_itest")),
        "item_name": to_str(row.get("item_name")),
        "issue_id": to_str(row.get("issue_id")),
        "issue_name": to_str(row.get("issue_name")),
        "set_type": to_str(row.get("set_type")),
        "item_type": to_str(row.get("item_type")),
        "answer_key": to_str(row.get("answer_key")),
        "admin_scoring_key": to_str(row.get("admin_scoring_key")),
        "fcp_specification": to_str(row.get("fcp_specification")),
        "admin_fcp_specification": to_str(row.get("admin_fcp_specification")),
        "fs_task": to_str(row.get("fs_task")),
        "admin_fs_task": to_str(row.get("admin_fs_task")),
        "starred_status": to_str(row.get("starred_status")),
        "admin_starred_status": to_str(row.get("admin_starred_status")),
        "admin_subscore_category": to_str(row.get("admin_subscore_category")),
        "total_word_count": to_int(row.get("total_word_count")),
        "author": to_str(row.get("author")),
        "author_date": to_int(row.get("author_date")),
        "completed_usage_count": to_int(row.get("completed_usage_count")),
        "next_scheduled_admin_name": to_str(row.get("next_scheduled_admin_name")),
        "stage": to_str(row.get("stage")),
        "stage_reason": to_str(row.get("stage_reason")),
        "gender": to_str(row.get("gender")),
        "admin_equating_form_name": to_str(row.get("admin_equating_form_name")),
        "admin_weight": to_int(row.get("admin_weight")),
        "admin_max_points": to_int(row.get("admin_max_points")),
        "admin_scoring_max_points": to_int(row.get("admin_scoring_max_points")),
        "admin_grading_tolerance": to_int(row.get("admin_grading_tolerance")),
        "admin_usage_code": to_str(row.get("admin_usage_code")),
        "admin_actual_usage_code": to_str(row.get("admin_actual_usage_code")),
        "admin_element_code": to_int(row.get("admin_element_code")),
        "admin_actual_element_code": to_int(row.get("admin_actual_element_code")),
        "admin_stats_level": to_str(row.get("admin_stats_level")),
    }