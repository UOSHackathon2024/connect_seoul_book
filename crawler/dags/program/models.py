from typing import Optional
from datetime import date

class Program:
    def __init__(
        self,
        program_id: Optional[int] = None,
        program_name: str = '',
        library_name: str = '',
        start_program: Optional[date] = None,
        end_program: Optional[date] = None,
        accept_start: Optional[date] = None,
        accept_end: Optional[date] = None,
        category: Optional[str] = None,
        client_type: Optional[str] = None,
        program_place: Optional[str] = None,
        program_instructor: Optional[str] = None,
        image_url: Optional[str] = None,
        program_url: Optional[str] = None
    ):
        self.program_id = program_id
        self.program_name = program_name
        self.library_name = library_name
        self.start_program = start_program
        self.end_program = end_program
        self.accept_start = accept_start
        self.accept_end = accept_end
        self.category = category
        self.client_type = client_type
        self.program_place = program_place
        self.program_instructor = program_instructor
        self.image_url = image_url
        self.program_url = program_url

    def __repr__(self):
        return (
            f"Program(program_id={self.program_id}, program_name='{self.program_name}', "
            f"start_program={self.start_program}, end_program={self.end_program}, "
            f"accept_start={self.accept_start}, accept_end={self.accept_end}, "
            f"category='{self.category}', days='{self.days}', client_type='{self.client_type}', "
            f"program_place='{self.program_place}', program_instructor='{self.program_instructor}', "
            f"image_url='{self.image_url}')"
        )
