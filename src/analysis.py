import matplotlib.pyplot as plt
import seaborn as sns

def display_basic_info(df):
    print(df.info())

def calculate_basic_metrics(df):
    return df.describe()

def non_graphical_univariate_analysis(df):
    return df.mad()

def graphical_univariate_analysis(df, quantitative_variables):
    for variable in quantitative_variables:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[variable], kde=True)
        plt.title(f'Histogram for {variable}')
        plt.xlabel(variable)
        plt.ylabel('Frequency')
        plt.savefig(f'results/histograms/{variable}_histogram.png')
        plt.close()

def bivariate_analysis(df, applications):
    for app in applications:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=f'{app}_DL_data', y='Total_DL_data', data=df, label=f'{app} DL')
        sns.scatterplot(x=f'{app}_UL_data', y='Total_UL_data', data=df, label=f'{app} UL')
        plt.title(f'Relationship between {app} and Total DL+UL Data')
        plt.xlabel(f'Total {app} Data')
        plt.ylabel('Total DL+UL Data')
        plt.legend()
        plt.savefig(f'results/scatter_plots/{app}_scatter_plot.png')
        plt.close()

def display_user_aggregated_plots(user_aggregated):
    # Set the style for seaborn
    sns.set(style="whitegrid")

    # Plotting the Number of xDR sessions per user
    plt.figure(figsize=(12, 6))
    sns.barplot(x=user_aggregated['Number_of_xDR_sessions'].values, y=user_aggregated.index, palette="viridis")
    plt.title('Number of xDR Sessions per User')
    plt.xlabel('Number of Sessions')
    plt.ylabel('User')
    plt.show()

    # Plotting the Session duration per user
    plt.figure(figsize=(12, 6))
    sns.barplot(x=user_aggregated['Session_duration'].values, y=user_aggregated.index, palette="viridis")
    plt.title('Session Duration per User')
    plt.xlabel('Session Duration (ms)')
    plt.ylabel('User')
    plt.show()

    # Plotting the Total DL data per user
    plt.figure(figsize=(12, 6))
    sns.barplot(x=user_aggregated['Total_DL_data'].values, y=user_aggregated.index, palette="viridis")
    plt.title('Total Download Data per User')
    plt.xlabel('Total Download Data (Bytes)')
    plt.ylabel('User')
    plt.show()

    # Plotting the Total UL data per user
    plt.figure(figsize=(12, 6))
    sns.barplot(x=user_aggregated['Total_UL_data'].values, y=user_aggregated.index, palette="viridis")
    plt.title('Total Upload Data per User')
    plt.xlabel('Total Upload Data (Bytes)')
    plt.ylabel('User')
    plt.show()