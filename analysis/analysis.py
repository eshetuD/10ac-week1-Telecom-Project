import pandas as pd

def display_top_handsets(df, top_n=10):
    """
    Display the top N handsets used by customers.

    Parameters:
    - df_clean (pd.DataFrame): DataFrame containing clean data.
    - top_n (int): Number of top handsets to display.

    Returns:
    - pd.Series: Top handsets series.
    """
    top_handsets = df['Handset Type'].value_counts().head(top_n)
    print(f"Top {top_n} Handsets:")
    print(top_handsets)
    return top_handsets

def display_top_manufacturers(df, top_n=3):
    """
    Display the top N handset manufacturers.

    Parameters:
    - df_clean (pd.DataFrame): DataFrame containing clean data.
    - top_n (int): Number of top manufacturers to display.

    Returns:
    - pd.Series: Top manufacturers series.
    """
    top_manufacturers = df['Handset Manufacturer'].value_counts().head(top_n)
    print(f"\nTop {top_n} Handset Manufacturers:")
    print(top_manufacturers)
    return top_manufacturers

def display_top_manufacturer_handsets(df, top_manufacturers=3, top_handsets=5):
    """
    Display the top N handsets per top M handset manufacturers.

    Parameters:
    - df_clean (pd.DataFrame): DataFrame containing clean data.
    - top_manufacturers (int): Number of top manufacturers to consider.
    - top_handsets (int): Number of top handsets to display for each manufacturer.

    Returns:
    - pd.Series: Top handsets series.
    """
    top_manufacturer_handsets = df.groupby('Handset Manufacturer')['Handset Type'].value_counts().groupby(level=0, group_keys=False).nlargest(top_handsets)
    print(f"\nTop {top_handsets} Handsets per Top {top_manufacturers} Manufacturers:")
    print(top_manufacturer_handsets.head())
    return top_manufacturer_handsets

