from sqlalchemy import create_engine, text

def set_data_to_dict(data_list):
    
    result = []
    for data in data_list:
        result.append(
            {
                'name': data[0],
                'lng': data[1],
                'lat':data[2],
                'is_connected': data[3]
            }
        )
    
    return result
    

def load(db_conn_str:str, data_list:list):
    """
    list should be like [(id, name, lng, lat)]
    """
    
    batch = set_data_to_dict(data_list)
    
    engine = create_engine(db_conn_str)
    
    with engine.begin() as conn:
        
        conn.execute(
            text(
            """
            INSERT INTO library(library_name, longitude, latitude, is_connected)
            VALUES(:name, :lng, :lat, :is_connected)
            """),
            batch
        )