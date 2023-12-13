from data_loader import load_data_from_postgres
from data_preprocessing import handle_missing_values
from analysis import (
    display_basic_info,
    calculate_basic_metrics,
    non_graphical_univariate_analysis,
    graphical_univariate_analysis,
    bivariate_analysis,
)

def main():
    # Connect to PostgreSQL using SQLAlchemy and load data
    postgres_config = {
        'host': 'localhost',
        'database': 'telecom',
        'user': 'postgres',
        'password': 'root',
        'port': '5432',
        'table_name': 'xdr_data',
    }
    df = load_data_from_postgres(**postgres_config)

    # Data Preprocessing
    df = handle_missing_values(df)

    # Exploratory Data Analysis
    display_basic_info(df)

    # Basic Metrics
    basic_metrics = calculate_basic_metrics(df)
    print("\nBasic Metrics:")
    print(basic_metrics)

    # Non-Graphical Univariate Analysis
    dispersion_params = non_graphical_univariate_analysis(df)
    print("\nDispersion Parameters:")
    print(dispersion_params)

    # Graphical Univariate Analysis
    quantitative_variables = ['Session_duration', 'Total_DL_data', 'Total_UL_data']
    graphical_univariate_analysis(df, quantitative_variables)

    # Bivariate Analysis
    applications = ['Social_Media', 'Google', 'Email', 'Youtube', 'Netflix', 'Gaming', 'Other']
    bivariate_analysis(df, applications)

    # User Aggregated Plots
    user_aggregated = df.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',
        'Dur. (ms).1': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum',
        'Social Media DL (Bytes)': 'sum',
        'Social Media UL (Bytes)': 'sum',
        'Google DL (Bytes)': 'sum',
        'Google UL (Bytes)': 'sum',
        'Email DL (Bytes)': 'sum',
        'Email UL (Bytes)': 'sum',
        'Youtube DL (Bytes)': 'sum',
        'Youtube UL (Bytes)': 'sum',
        'Netflix DL (Bytes)': 'sum',
        'Netflix UL (Bytes)': 'sum',
        'Gaming DL (Bytes)': 'sum',
        'Gaming UL (Bytes)': 'sum',
        'Other DL (Bytes)': 'sum',
        'Other UL (Bytes)': 'sum',
    })

    # Rename columns for clarity
    user_aggregated = user_aggregated.rename(columns={
        'Bearer Id': 'Number_of_xDR_sessions',
        'Dur. (ms).1': 'Session_duration',
        'Total DL (Bytes)': 'Total_DL_data',
        'Total UL (Bytes)': 'Total_UL_data',
        'Social Media DL (Bytes)': 'Social_Media_DL_data',
        'Social Media UL (Bytes)': 'Social_Media_UL_data',
        'Google DL (Bytes)': 'Google_DL_data',
        'Google UL (Bytes)': 'Google_UL_data',
        'Email DL (Bytes)': 'Email_DL_data',
        'Email UL (Bytes)': 'Email_UL_data',
        'Youtube DL (Bytes)': 'Youtube_DL_data',
        'Youtube UL (Bytes)': 'Youtube_UL_data',
        'Netflix DL (Bytes)': 'Netflix_DL_data',
        'Netflix UL (Bytes)': 'Netflix_UL_data',
        'Gaming DL (Bytes)': 'Gaming_DL_data',
        'Gaming UL (Bytes)': 'Gaming_UL_data',
        'Other DL (Bytes)': 'Other_DL_data',
        'Other UL (Bytes)': 'Other_UL_data'
    })

    # Display the aggregated information per user
    print(user_aggregated)

    # User Aggregated Plots
    display_user_aggregated_plots(user_aggregated)

if __name__ == "__main__":
    main()
