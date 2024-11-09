"""
기본정보 추출

library_id	Long
library_name	String
isconnected	boolean
longitude	Double
latitude	Double    

https://www.data.go.kr/tcs/dss/selectStdDataDetailView.do

"""
import pandas as pd
from library.models import Library, BookConnection
from datetime import datetime

from sqlalchemy import create_engine, text

from airflow.hooks.base import BaseHook
from airflow.utils.log.logging_mixin import LoggingMixin

class LibraryHook(BaseHook, LoggingMixin):
    
    def __init__(
        self, 
        db_conn_str: str,
        file_src_path: str,
        *args, 
        **kwargs
    ):
        super(LibraryHook, self).__init__(*args, **kwargs)
        self.db_conn_str    = db_conn_str
        self.file_path      = file_src_path
        
    def delete_old_info(self):
        
        engine = create_engine(self.db_conn_str)
        
        with engine.begin() as conn:
            
            conn.execute(
                text(
                """
                DELETE FROM library
                """
                )
            )
        
    def get_info_batch(self) -> list[Library]:
        
        df = pd.read_csv(self.file_path, encoding="euc-kr")
        
        df = df.loc[df['시도명'] == '서울특별시']
        
        df = df[[
            '시군구명', '도서관명', '위도', '경도', '소재지도로명주소', 
            '평일운영시작시각', '평일운영종료시각', '토요일운영시작시각', '토요일운영종료시각', '공휴일운영시작시각', '공휴일운영종료시각'
            ]] # '시군구명'
        
        df = df.dropna(subset = ['도서관명', '위도', '경도'])
        
        result = []
        
        size = len(df)
        for i in range(0, size):
            #data = df.iloc[i, 0]+df.iloc[i, 3]
            
            #district = df.iloc[i, 0]
            lib = Library(
                library_id = None,
                library_name = df.iloc[i, 1],
                is_connected = False,
                longitude = float(df.iloc[i, 2]),
                latitude = float(df.iloc[i, 3]),
                start_time_day = datetime.strptime(df.iloc[i, 5], "%H:%M").time(),
                end_time_day = datetime.strptime(df.iloc[i, 6], "%H:%M").time(),
                start_time_weekend = datetime.strptime(df.iloc[i, 7], "%H:%M").time(),
                end_time_weekend = datetime.strptime(df.iloc[i, 8], "%H:%M").time(),
                start_time_holiday = datetime.strptime(df.iloc[i, 9], "%H:%M").time(),
                end_time_holiday = datetime.strptime(df.iloc[i, 10], "%H:%M").time()
            ) # this obj should be transformed as date types
            
            result.append(
                lib
            )
            
        return result
    
    def save_library_batch(self, batch:list[Library]):
        
        engine = create_engine(self.db_conn_str)

        batch = [library.__dict__ for library in batch]
        
        with engine.begin() as conn:
            
            conn.execute(
                text(
                """
                INSERT INTO library(
                        library_name, 
                        longitude, 
                        latitude, 
                        is_connected,
                        start_time_day,
                        end_time_day,
                        start_time_weekend,
                        end_time_weekend,
                        start_time_holiday,
                        end_time_holiday
                    )
                VALUES(
                        :library_name, 
                        :longitude, 
                        :latitude, 
                        :is_connected,
                        :start_time_day,
                        :end_time_day,
                        :start_time_weekend,
                        :end_time_weekend,
                        :start_time_holiday,
                        :end_time_holiday
                    )
                """),
                batch
            )
    

class BookConnectionHook(BaseHook, LoggingMixin):
    
    def __init__(self, file_src_path, *args, **kwargs):
        super(BookConnectionHook, self).__init__(*args, **kwargs)
        self.file_path = file_src_path
        
    def get_info_batch(self) -> list[BookConnection]:
        """
        returns like [('도서관명','주소')]
        """
        df = pd.read_csv(self.file_path, encoding="euc-kr")
        df = df[['도서관명', '주소']] #'운영상태'
        
        df = df.dropna()
        
        result = []
        
        size = len(df)
        for i in range(0, size):
            
            result.append(
                BookConnection(
                    library_name = df.iloc[i, 0],
                    library_addr = df.iloc[i, 1]
                )
            )
            
        return result