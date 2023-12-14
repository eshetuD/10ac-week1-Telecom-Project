from sqlalchemy import create_engine
import pandas as pd

def connect_and_read_data(database_name, table_name, connection_params):
    """
    Connect to the database and retrieve data from the specified table.

    Parameters:
    - database_name (str): Name of the database.
    - table_name (str): Name of the table.
    - connection_params (dict): Dictionary containing connection parameters.

    Returns:
    - pd.DataFrame: DataFrame containing the data from the specified table.
    """
    engine = create_engine(
        f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{database_name}"
    )

    sql_query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(sql_query, con=engine)
    
    return df