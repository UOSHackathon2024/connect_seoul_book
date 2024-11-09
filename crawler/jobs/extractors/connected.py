import pandas as pd

def extract(file_path):
    """
    returns like [('도서관명','주소')]
    """
    df = pd.read_csv(file_path, encoding="euc-kr")
    df = df[['도서관명', '주소', '운영상태']]
    
    df = df.dropna()
    
    result = []
    
    size = len(df)
    for i in range(0, size):
        
        name = df.iloc[i, 0]
        addr = df.iloc[i, 1].split()[-1]
        
        
        result.append((
            name,
            addr
        ))
        
    return result