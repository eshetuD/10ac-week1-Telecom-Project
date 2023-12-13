def handle_missing_values(df):
    df.fillna(df.mean(), inplace=True)
    return df



    # Convert columns to numeric, coercing errors to NaN
    numeric_df = df.apply(pd.to_numeric, errors='coerce')

    # Calculate the mean of each column
    mean_values = numeric_df.mean()

    # Fill missing values with the mean of each column
    filled_data_frame = numeric_df.fillna(mean_values)
    return filled_data_frame
    #df_fill.fillna(df_fill.mean(), inplace=True)