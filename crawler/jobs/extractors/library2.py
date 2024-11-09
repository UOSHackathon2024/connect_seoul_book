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


def extract(
    file_path
    ):
    """
    returns a list of tuples:
    [(district, name, x, y),  ...]
    """
    df = pd.read_csv(file_path, encoding="euc-kr")
    df = df.loc[df['시도명'] == '서울특별시']
    df = df[['시군구명', '도서관명', '위도', '경도', '소재지도로명주소']] # '시군구명'
    df = df.dropna()
    
    result = []
    
    size = len(df)
    for i in range(0, size):
        #data = df.iloc[i, 0]+df.iloc[i, 3]
        
        #district = df.iloc[i, 0]
        name = df.iloc[i, 1]
        lng = float(df.iloc[i, 2])
        lat = float(df.iloc[i, 3])
        addr = df.iloc[i, 4]
        
        
        result.append(
            (name, lng, lat, addr)
        )
        
        # assert dist not in check, f"{data}"
        # check.add(data)
        #print(df.iloc[0, 0])
    return result
    