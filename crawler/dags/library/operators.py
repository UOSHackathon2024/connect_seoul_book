from library.models import Library, BookConnection
from library.hooks import LibraryHook, BookConnectionHook

from airflow.models import BaseOperator
from airflow.utils.log.logging_mixin import LoggingMixin
from difflib import SequenceMatcher

class DeleteOldInfo(BaseOperator, LoggingMixin):
    
    def __init__(
        self,
        db_conn_str: str,
        *args,
        **kwargs
    ):
        super(DeleteOldInfo, self).__init__(*args, **kwargs)
        self.db_conn_str = db_conn_str
        
    def execute(self, context):
        
        hook_lib = LibraryHook(
            self.db_conn_str,
            None
        )
        
        hook_lib.delete_old_info()
        
    

class UploadLibraryToDB(BaseOperator, LoggingMixin):
    
    def __init__(
        self,
        db_conn_str: str,
        path_library_info_file:str,
        path_book_conn_info_file:str,
        similarity_check_threshold:float = 0.8,
        *args, 
        **kwargs
    ):
        super(UploadLibraryToDB, self).__init__(*args, **kwargs)
        self.db_conn_str = db_conn_str
        
        self.path_library_info_file     = path_library_info_file
        self.path_book_conn_info_file   = path_book_conn_info_file
        self.similarity_check_threshold = similarity_check_threshold
        
    def execute(self, context):
        
        hook_lib = LibraryHook(
            self.db_conn_str,
            self.path_library_info_file
        )
        
        hook_conn = BookConnectionHook(
            self.path_book_conn_info_file
        )
        
        batch_lib: list[Library]            = hook_lib.get_info_batch()
        batch_conn: list[BookConnection]    = hook_conn.get_info_batch()
        
        batch_lib = self.transform(
                batch_lib=batch_lib, 
                batch_conn=batch_conn
            )        
        
        hook_lib.save_library_batch(batch_lib)
    
    def transform(
        self, 
        batch_lib:list[Library], 
        batch_conn:list[BookConnection]) -> list[Library]:
        
        result = []
    
        for lib in batch_lib:
                
            for conn in batch_conn:
                
                lib.is_connected = self.check_connection(
                    lib.library_name,
                    conn.library_name
                )
                
                if lib.is_connected:
                    break
            
            result.append(
                lib
            )
                
                
        return result
    
    def check_connection(self, origin_lib_name, conn_lib_name):
    
        threshold = self.similarity_check_threshold
        
        sim = self.sim_bw_str(origin_lib_name, conn_lib_name.split()[-1])
        
        if sim > threshold:
            return True
    
        return False
        
    def sim_bw_str(self, str_a, str_b):
        
        return SequenceMatcher(None, str_a, str_b).ratio()
        