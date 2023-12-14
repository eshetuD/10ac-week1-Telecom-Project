from database_conn.db_connector import connect_and_read_data
from data_preprocessing.data_processor import handle_null_values, process_categorical_data, process_numeric_data
from analysis.analysis import display_top_handsets, display_top_manufacturers, display_top_manufacturer_handsets

# Define connection parameters
database_name = 'telecom'
table_name = 'xdr_data'
connection_params = {
    "host": "localhost",
    "user": "postgres",
    "password": "root",
    "port": "5432",
    "database": "telecom"
}

# Connect to the database and read data
df = connect_and_read_data(database_name, table_name, connection_params)

#Handling Null Values
df = handle_null_values(df, threshold=50)

# Process categorical data
df = process_categorical_data(df)

#Process Numeric data
process_numeric_data(df)

# Display top 10 handsets
display_top_handsets(df_clean, top_n=10)

# Display Top 3 Handset Manufacturer
display_top_manufacturers(df_clean, top_n=3)

# Display the top 5 handsets per top 3 handset manufacturers
display_top_manufacturer_handsets(df_clean, top_manufacturers=3, top_handsets=5)



