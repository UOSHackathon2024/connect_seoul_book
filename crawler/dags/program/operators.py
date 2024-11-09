from playwright.sync_api import sync_playwright, Playwright
from program.models import Program
from program.hooks import ProgramDBHook

from airflow.models import BaseOperator
from airflow.utils.log.logging_mixin import LoggingMixin

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
        
        hook_lib = ProgramDBHook(
            self.db_conn_str
        )
        
        hook_lib.delete_old_info()

class CrawlProgramPage(BaseOperator, LoggingMixin):
    
    def __init__(
        self, 
        db_conn_str: str,
        page_url: str,
        *args,
        **kwargs
    ):
        super(CrawlProgramPage, self).__init__(*args, **kwargs)
        
        self.db_conn_str        = db_conn_str
        self.page_url           = page_url
        self.image_url_prefix   = "https://lib.sen.go.kr"
        
    def execute(self, context):
        self.log.info("execute started")
        
        with sync_playwright() as playwright:
            result = self.crawl(playwright)
        
        self.log.info("got crawling result")
        
        hook = ProgramDBHook(self.db_conn_str)
        self.log.info("connected hook")
        
        hook.save_program_batch(result)
        self.log.info("saved")
            
    def crawl(self, playwright:Playwright) -> list[Program]:
        
        chromium = playwright.chromium
        browser = chromium.launch()
        page = browser.new_page()
        
        page.goto(self.page_url)
        
        program_list = page.locator('xpath=//*[@id="teach"]/ul/a').all()
        
        result = []
        
        for loc in program_list:
            page_result = self.crawl_by_program(page, loc)
            if page_result is not None:
                result.append(page_result)
        
        browser.close()
        
        return result
            
    def crawl_by_program(self, page, loc):
        
        try:
            image = loc.locator('xpath=//li/div[1]/img')
        except:
            image = None
        
        # program name cannot be null
        try:
            program_name = image.get_attribute('title')
        except:
            return None
            
        try:
            image_url = self.image_url_prefix + image.get_attribute('src')
        except:
            image_url = None
            
        try:
            library_name = loc.locator('xpath=//li/div[2]/ul/li[1]').inner_text().split()[-1]
        except:
            library_name = None
        
        try:
            start_end_program = loc.locator('xpath=//li/div[2]/ul/li[2]').inner_text()
            start_program, end_program = start_end_program[4:25].split('~')
        except:
            start_program, end_program = None, None
            
        # try:
        #     accept_start_end = loc.locator('xpath=//li/div[2]/ul/li[3]').inner_text()
        #     accept_start, accept_end = accept_start_end[4:25].split('~')
        # except:
        #     accept_start, accept_end = None, None  
        
        try:
            image.click()
        except:
            pass
        
        # -------------- new page
        try:
            tbody = page.locator('xpath=//*[@id="teach_table"]/tbody')
        except:
            pass
        
        try:
            accept_start_end = page.locator('xpath=//*[@id="teach_table"]/tbody/tr[2]/td').inner_text()
            accept_start, accept_end = accept_start_end.split('~')
            
            def lamb(str_dt):
                str_dt = str_dt.split()
                if len(str_dt[1]) < 5:
                    str_dt[1] = '0' + str_dt[1]
                return str_dt[0] + ' ' + str_dt[1] + ':00'

            accept_start = lamb(accept_start)
            accept_end = lamb(accept_end)
        except:
            accept_start, accept_end = None, None  
            
        try:
            # //*[@id="teach_table"]/tbody/tr[1]/td
            category = page.locator('xpath=//*[@id="teach_table"]/tbody/tr[1]/td').inner_text()
        except:
            category = None
            
        # 강의 대상
        try:
            client_type = tbody.locator('xpath=//tr[@class="mAllpx"][1]/td[last()]').inner_text()
        except:
            client_type = None
            
        # 강의 장소
        try:
            program_place = tbody.locator('xpath=//tr[@class="mAllpx"][3]/td[1]').inner_text()
        except:
            program_place = None
                
        # 강사명
        try:
            program_instructor = tbody.locator('xpath=//tr[@class="mAllpx"][3]/td[last()]').inner_text()
        except:
            program_instructor = None
        
        # program url
        try:
            program_url = page.url
        except:
            program_url = None
                
        program = Program(
                program_id=None,
                program_name=program_name,
                library_name=library_name,
                start_program = start_program,
                end_program = end_program,
                accept_start = accept_start,
                accept_end = accept_end,
                category = category,
                client_type = client_type,
                program_place = program_place,
                program_instructor = program_instructor,
                image_url = image_url,
                program_url=program_url
            )
            
        page.go_back()
        return program