REQUIRED_FIELDS = [
    "source",
    "uploaded_by",
    "file_type"
]

REQUIRED_SHEET_COLUMNS = [
    "admin_name",
    "admin_form_name",
    "admin_pretest_form_name",
    "admin_session_id",
    "admin_base_session_item_num",
    "admin_scram_session_item_num",
    "set_id",
    "set_name",
    "item_id",
    "item_id_itest",
    "item_name",
    "issue_id",
    "issue_name",
    "set_type",
    "item_type",
    "answer_key",
    "admin_scoring_key",
    "fcp_specification",
    "admin_fcp_specification",
    "fs_task",
    "admin_fs_task",
    "starred_status",
    "admin_starred_status",
    "admin_subscore_category",
    "total_word_count",
    "author",
    "author_date",
    "completed_usage_count",
    "next_scheduled_admin_name",
    "stage",
    "stage_reason",
    "gender",
    "admin_equating_form_name",
    "admin_weight",
    "admin_max_points",
    "admin_scoring_max_points",
    "admin_grading_tolerance",
    "admin_usage_code",
    "admin_actual_usage_code",
    "admin_element_code",
    "admin_actual_element_code",
    "admin_stats_level"
]

ROW_REQUIRED_FIELDS  = {
    "admin_name": str,
    "admin_form_name": str,
    "admin_pretest_form_name": str,
    "admin_session_id": int,
    "admin_base_session_item_num": str,
    "admin_scram_session_item_num": str,
    "set_id": str,
    "set_name": str,
    "item_id": str,
    "item_id_itest": str,
    "item_name": str,
    "issue_id": str,
    "issue_name": str,
    "set_type": str,
    "item_type": str,
    "answer_key": str,
    "admin_scoring_key": str,
    "fcp_specification": str,
    "admin_fcp_specification": str,
    "fs_task": str,
    "admin_fs_task": str,
    "starred_status": str,
    "admin_starred_status": str,
    "admin_subscore_category": str,
    "total_word_count": int,
    "author": str,
    "author_date": int,
    "completed_usage_count": int,
    "next_scheduled_admin_name": str,
    "stage": str,
    "stage_reason": str,
    "gender": str,
    "admin_equating_form_name": str,
    "admin_weight": int,
    "admin_max_points": int,
    "admin_scoring_max_points": int,
    "admin_grading_tolerance": int,
    "admin_usage_code": str,
    "admin_actual_usage_code": str,
    "admin_element_code": int,
    "admin_actual_element_code": int,
    "admin_stats_level": str
}

ENABLE_ROW_VALIDATION = True

ROW_FIELD_RULES = {
    "admin_name": {
        "type": "string",
        "nullable": False
    },
    "admin_form_name": {
        "type": "string",
        "nullable": False
    },

    "admin_session_id": {
        "type": "number",
        "nullable": False
    },
}

USE_AWS_SECRETS = True  # LOCAL DEVELOPMENT FLAG


