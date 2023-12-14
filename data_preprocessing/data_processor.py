import pandas as pd

def handle_null_values(df, threshold=0.5):
    """
    Display null percentage for each column and remove columns with more than the specified threshold of null values.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - threshold (float): Threshold for null values percentage. Columns exceeding this threshold will be removed.

    Returns:
    - pd.DataFrame: DataFrame with columns having less than the specified threshold of null values.
    """
    null_percentage = (df.isnull().mean() * 100).sort_values(ascending=False)
    print("Null Percentage for Each Column:")
    print(null_percentage)

    # Remove columns with more than the specified threshold of null values
    columns_to_remove = null_percentage[null_percentage > threshold].index
    df = df.drop(columns=columns_to_remove)

    print(f"\nColumns removed with more than {threshold}% null values:")
    print(columns_to_remove)

    return df



def process_categorical_data(df):
    """
    Extract categorical data and fill missing values with mode.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.

    Returns:
    - pd.DataFrame: DataFrame with processed categorical data.
    """
    category_data = df.select_dtypes(include=['object'])

    # Fill missing values with mode for each column
    for column in category_data.columns:
        df[column] = category_data[column].fillna(category_data[column].mode()[0])

    return df


def process_numeric_data(df):
    """
    Extract numeric data and fill missing values with mean.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.

    Returns:
    - pd.DataFrame: DataFrame with processed numeric data.
    """
    # Drop columns with non-numeric data types
    numeric_df = df.select_dtypes(include=['number'])

    # Calculate the mean of each column
    mean_values = numeric_df.mean()

    # Fill missing values with the mean of each column
    for column in numeric_df.columns:
        df[column] = numeric_df.fillna(mean_values)

    return df

