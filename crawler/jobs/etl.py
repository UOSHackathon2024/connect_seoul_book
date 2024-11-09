import extractors.library
import extractors.library2
import extractors.connected

import loaders.library
import os
#from dotenv import load_dotenv

def extract(
    api_key: str,
    ):
    
    # basic_info = extractors.library.extract(api_key) # list of (id, name, lng, lat)
    basic_info = extractors.library2.extract(
        "../source/name_lng_lat.csv"
    )
    
    is_connected = extractors.connected.extract(
        "../source/is_connected.CSV"
    )
    
    return basic_info, is_connected
        

def transform(basic_info, is_connected):
    """

    (name, lng, lat, addr)
    (name, addr)
    """
    # print(is_connected)
    result = []
    for lib in basic_info:
        con = False
        #if lib[0] in connected_addrs:
        for name, addr in is_connected:
            
            #print(lib[0], addr)
            if addr == lib[0]:
                con = True
                break
            
        
        result.append((
            lib[0],
            lib[1],
            lib[2],
            con,
        ))
            
    return result

    
def load(
    db_conn_str,
    data_list
    ):
    
    loaders.library.load(db_conn_str, data_list)
    


def main():
    conn_str = "mysql+pymysql://crawler:crawler@1.240.103.57:3018/hackathon"#hackathon"
    
    basic, connected_addrs = extract(
        "asd"
    )
    
    lib = transform(basic, connected_addrs)
    
    load(conn_str, lib)
    
    #print(raw_data)
if __name__ == "__main__":
    main()
    