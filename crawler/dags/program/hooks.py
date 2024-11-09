from airflow.hooks.base import BaseHook
from airflow.utils.log.logging_mixin import LoggingMixin

from sqlalchemy.engine import Engine
from sqlalchemy import create_engine, text
from program.models import Program

class ProgramDBHook(BaseHook, LoggingMixin):
    
    def __init__(self, conn_str, *args, **kwargs):
        
        super(ProgramDBHook, self).__init__(*args, **kwargs)
        
        self.engine = create_engine(conn_str)
        
    def get_engine(self) -> Engine:
        return self.engine
    
    def delete_old_info(self):
        
        with self.engine.begin() as conn:
            
            conn.execute(
                text(
                """
                DELETE FROM program
                """
                )
            )
    
    def save_program_batch(self, batch:list[Program]):
        
        batch = [program.__dict__ for program in batch]
        
        with self.engine.begin() as conn:
            
            conn.execute(
                text(
                """
                INSERT INTO program(
                    program_name,
                    library_name,
                    start_program,
                    end_program,
                    accept_start,
                    accept_end,
                    client_type,
                    category,
                    program_place,
                    program_instructor,
                    image_url,
                    program_url
                )
                VALUES(
                    :program_name,
                    :library_name,
                    :start_program,
                    :end_program,
                    :accept_start,
                    :accept_end,
                    :client_type,
                    :category,
                    :program_place,
                    :program_instructor,
                    :image_url,
                    :program_url
                )
                """
                ),
                batch
            )