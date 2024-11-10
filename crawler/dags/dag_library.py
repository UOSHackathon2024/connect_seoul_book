from datetime import datetime, timedelta
from airflow.decorators import dag, task, task_group
import os
import logging
from dotenv import load_dotenv
from library.operators import UploadLibraryToDB, DeleteOldInfo

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

logger = logging.getLogger(__name__)

default_args = {
    'owner'         : 'big-whale',
    'retries'       : 2,
    'retry_delay'   : timedelta(minutes=2)
}
        
@dag(
    dag_id = 'library-basic-updater',
    default_args=default_args,
    description= 'updating db for programs of seoul libraries',
    start_date = datetime(2024, 11,9),
    schedule_interval='@daily',
    concurrency = 3,
    max_active_runs = 1,
    catchup=False,
)
def workflow():
    
    db_conn_str = os.getenv('MYSQL_CONN_STR')
    path_library_info_file = os.path.realpath(os.path.join(os.path.dirname(__file__), '../source/library_info.csv'))
    path_book_conn_info_file = os.path.realpath(os.path.join(os.path.dirname(__file__), '../source/book_connection_info.csv'))
    
    task1 = DeleteOldInfo(
        db_conn_str=db_conn_str,
        task_id = 'delete_old_info_from_db'
    )
    
    task2 = UploadLibraryToDB(
        db_conn_str             =db_conn_str,
        path_library_info_file  =path_library_info_file,
        path_book_conn_info_file=path_book_conn_info_file,
        task_id='upload_library_to_db'
    )
    
    task1 >> task2
        
workflow()