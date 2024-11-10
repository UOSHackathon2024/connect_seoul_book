from typing import Optional
from datetime import time

class Library:
    def __init__(
        self,
        library_id: int,
        library_name: str,
        is_connected: bool,
        longitude: float,
        latitude: float,
        start_time_day: time,
        end_time_day: time,
        start_time_weekend: time,
        end_time_weekend: time,
        start_time_holiday: time,
        end_time_holiday: time,
        homepage_url:Optional[str] = None
    ):
        self.library_id: int = library_id
        self.library_name: str = library_name
        self.is_connected: bool = is_connected
        self.longitude: float = longitude
        self.latitude: float = latitude
        self.start_time_day: time = start_time_day
        self.end_time_day: time = end_time_day
        self.start_time_weekend: time = start_time_weekend
        self.end_time_weekend: time = end_time_weekend
        self.start_time_holiday: time = start_time_holiday
        self.end_time_holiday: time = end_time_holiday
        self.homepage_url = homepage_url

    def __repr__(self):
        return (
            f"Library(library_id={self.library_id}, library_name='{self.library_name}', "
            f"longitude={self.longitude}, latitude={self.latitude}, "
            f"start_time_day={self.start_time_day}, end_time_day={self.end_time_day}, "
            f"start_time_weekend={self.start_time_weekend}, end_time_weekend={self.end_time_weekend}, "
            f"start_time_holiday={self.start_time_holiday}, end_time_holiday={self.end_time_holiday})"
        )



class BookConnection:
    
    def __init__(
        self, 
        library_name: Optional[str] = None,
        library_addr: Optional[str] = None
    ):
        
        self.library_name = library_name
        self.library_addr = library_addr