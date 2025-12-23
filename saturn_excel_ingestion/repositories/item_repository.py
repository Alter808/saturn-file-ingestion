import pymysql
from services.aws_service import get_secret 
from constants import USE_AWS_SECRETS

INSERT_SQL = """
INSERT INTO px_item_attributes (
  admin_name,
  admin_form_name,
  admin_pretest_form_name,
  admin_session_id,
  admin_base_session_item_num,
  admin_scram_session_item_num,
  set_id,
  set_name,
  item_id,
  item_id_itest,
  item_name,
  issue_id,
  issue_name,
  set_type,
  item_type,
  answer_key,
  admin_scoring_key,
  fcp_specification,
  admin_fcp_specification,
  fs_task,
  admin_fs_task,
  starred_status,
  admin_starred_status,
  admin_subscore_category,
  total_word_count,
  author,
  author_date,
  completed_usage_count,
  next_scheduled_admin_name,
  stage,
  stage_reason,
  gender,
  admin_equating_form_name,
  admin_weight,
  admin_max_points,
  admin_scoring_max_points,
  admin_grading_tolerance,
  admin_usage_code,
  admin_actual_usage_code,
  admin_element_code,
  admin_actual_element_code,
  admin_stats_level
) VALUES (
  %(admin_name)s,
  %(admin_form_name)s,
  %(admin_pretest_form_name)s,
  %(admin_session_id)s,
  %(admin_base_session_item_num)s,
  %(admin_scram_session_item_num)s,
  %(set_id)s,
  %(set_name)s,
  %(item_id)s,
  %(item_id_itest)s,
  %(item_name)s,
  %(issue_id)s,
  %(issue_name)s,
  %(set_type)s,
  %(item_type)s,
  %(answer_key)s,
  %(admin_scoring_key)s,
  %(fcp_specification)s,
  %(admin_fcp_specification)s,
  %(fs_task)s,
  %(admin_fs_task)s,
  %(starred_status)s,
  %(admin_starred_status)s,
  %(admin_subscore_category)s,
  %(total_word_count)s,
  %(author)s,
  %(author_date)s,
  %(completed_usage_count)s,
  %(next_scheduled_admin_name)s,
  %(stage)s,
  %(stage_reason)s,
  %(gender)s,
  %(admin_equating_form_name)s,
  %(admin_weight)s,
  %(admin_max_points)s,
  %(admin_scoring_max_points)s,
  %(admin_grading_tolerance)s,
  %(admin_usage_code)s,
  %(admin_actual_usage_code)s,
  %(admin_element_code)s,
  %(admin_actual_element_code)s,
  %(admin_stats_level)s
)
"""

def insert_items(items: list[dict]):
    if USE_AWS_SECRETS:
        db_config = get_secret("saturn/ingest/dev", "us-east-1","saturn")
    else:
        db_config = {
            "user": "saturn_file_ingestor", 
            "password": "dK@L}0?2(7%c", 
            "host": "dev-saturn-mysql-cluster.cluster-cdm6igmm8pgv.us-west-2.rds.amazonaws.com", 
            "port": 3306, 
            "database": "saturn_december_e2e_2025"
        }
        
    conn = pymysql.connect(**db_config, autocommit=False)
    try:
        with conn.cursor() as cur:
            cur.executemany(INSERT_SQL, items)
        conn.commit()
        return len(items)
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()