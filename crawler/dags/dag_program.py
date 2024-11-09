from datetime import datetime, timedelta
from airflow.decorators import dag, task, task_group
import os
import logging
from dotenv import load_dotenv
from program.operators import DeleteOldInfo, CrawlProgramPage

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))


logger = logging.getLogger(__name__)

default_args = {
    'owner'         : 'big-whale',
    'retries'       : 2,
    'retry_delay'   : timedelta(minutes=2)
}
        
@dag(
    dag_id = 'library-programs-updater',
    default_args=default_args,
    description= 'updating db for programs of seoul libraries',
    start_date = datetime(2024, 11,9),
    schedule_interval='@daily',
    concurrency = 5,
    max_active_runs = 1,
    catchup=False,
)
def workflow():
    
    db_conn_str = os.getenv('MYSQL_CONN_STR')
    
    task1 = DeleteOldInfo(
        db_conn_str=db_conn_str,
        task_id = 'delete_old_info_from_db'
    )
    
    # task 2
    max_num_crawl_pages = 6
    tasks = []
    
    for i in range(1, max_num_crawl_pages + 1):
        
        page_url = f"https://lib.sen.go.kr/lib/module/teach/index.do?teach_idx=0&editMode=ADD&menu_idx=11&homepage_id=h24&large_category_idx=0&group_idx=0&category_idx=0&_program_age_div_arr=on&viewPage={i}"
        
        
        operator = CrawlProgramPage(
            db_conn_str=db_conn_str,
            page_url=page_url,
            task_id = f"crawling_program_page_{i}"
        )
        
        tasks.append(operator)
    
    task1 >> tasks        
    
    
    
workflow()
    
    
    
    