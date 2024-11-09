"""
기본정보 추출

library_id	Long
library_name	String
isconnected	boolean
longitude	Double
latitude	Double    


기본 정보: http://openapi.seoul.go.kr:8088/sample/xml/SeoulPublicLibraryInfo/1/5/
책이음 서비스 확인: https://books.nl.go.kr/PU/contents/P40401000000.do?areaCode=11&schM=list&page=1&schFld=libNm&schStr=&pageCount=10&schDiv=

"""
import xml.etree.ElementTree as ET
import requests

def crawl_data(url):
    
    req = requests.get(url)
    if req is None:
        return []
    
    xml_root = ET.fromstring(req.text)
    rows = xml_root.findall("row")
    
    result = []
    
    for row in rows:    
        lib_id = row.find("LBRRY_SEQ_NO").text
        name = row.find("LBRRY_NAME").text
        long = float(row.find("XCNTS").text)
        lat = float(row.find("YDNTS").text)
        
        result.append((lib_id, name, long, lat))
        
    return result

def extract(
    api_key: str = "566a6d5154706c613130364449494758"
    
    ):
    """
    returns a list of tuples:
    [(id, name, x, y),  ...]
    566a6d5154706c613130364449494758
    """
    urls = [
        f"http://openapi.seoul.go.kr:8088/{api_key}/xml/SeoulPublicLibraryInfo/{start}/{start+100-1}/" for start in range(1, 999, 100) 
    ]
    
    result = []
    
    for url in urls:
        result += crawl_data(url)
        
    return result
    