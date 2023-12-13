import pandas as pd
from sqlalchemy import create_engine

def load_data_from_postgres(host, database, user, password, port, table_name):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    query = f'SELECT * FROM {table_name};'
    df = pd.read_sql(query, engine)
    engine.dispose()
    return df