import pandas as pd

url="https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
df=pd.read_csv(url)            

if df is None or df.empty:
    print("Error: DataFrame is empty or not loaded correctly.")
else:
    print("Data loaded successfully!")

print(df.head())

print("columns:",df.columns)

# Ensures 'date' column exists before converting to datetime
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  
    print(" 'date' column converted to datetime.")
else:
    print(" 'date' column not found in dataset.")


print("Dataset shape:", df.shape)  # gives no.of rows and columns 

print(df.dtypes)

# summary statistics
print(df.describe())


# data cleaning and preprocessing

# handling missing values
print(df.isnull().sum())

# fill missing values with 0
df.fillna(0,inplace=True)

# convert date column to date time format
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
else:
    print(" 'date' column not found in dataset.")



# data analysis and insights

# get latest date in dataset
latest_date = df['date'].max()
print("Latest date in dataset:", latest_date)

# filter data for latest date
latest_data=df[df['date']==latest_date]

# select top 10 countries with highest cases
if 'total_cases' in df.columns:
    top_countries = latest_data.nlargest(10, 'total_cases')
    print(top_countries[['country', 'total_cases']])
else:
    print(" 'total_cases' column not found.")





# analyze case growth over time in India

import matplotlib.pyplot as plt
import seaborn as sns

# filter for specific country
if 'country' in df.columns and 'total_cases' in df.columns and 'total_deaths' in df.columns:
    india_data = df[df['country'] == "India"]
    print(india_data.head())

    # Plot total cases over time
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=india_data['date'], y=india_data['total_cases'], label="Total Cases")
    sns.lineplot(x=india_data['date'], y=india_data['total_deaths'], label="Total Deaths", color='red')

    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.title("COVID-19 Cases and Deaths in India")
    plt.legend()
    plt.xticks(rotation=45)  # rotates dates labels on x axis to 45 degrees for readability
    plt.show()
else:
     print("Required columns for India's case analysis are missing!")


# Get unique country names
if 'country' in df.columns:
    country_list = df["country"].unique()
    print(country_list)
else:
    print(" 'country' column is missing!")


# calculate recovery rate
if 'total_cases' in df.columns and 'total_deaths' in df.columns:
    df['recovery_rate']=(df['total_cases']-df['total_deaths'])/df['total_cases'] * 100
    df['recovery_rate'].fillna(0, inplace=True)
    print(df[['country', 'date', 'total_cases', 'total_deaths', 'recovery_rate']].head())
else:
    print(" 'total_cases' or 'total_deaths' column is missing!")



# Data Visualization

# comapre covid-19 cases for multiple countries
countries=["India", "United Kingdom", "Germany"]
if 'country' in df.columns and 'total_cases' in df.columns:
    df_filtered=df[df['country'].isin(countries)]

    # creating the figure
    plt.figure(figsize=(10,5))

    # plotting the line graph
    sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='country')

    # labelling and formatting
    plt.xlabel("Date")
    plt.ylabel("Total_cases")
    plt.title("COVID-19 cases over time for selected countries")

    # adding a legend
    plt.legend()

    # formatting the x-axis ticks
    plt.xticks(rotation=45)

    # displaying the plot
    plt.show()
else:
    print("Required columns for multiple country comparison are missing!")


# Visualizing recovery rate

# top 10 countries by recovery rate
if 'total_cases' in df.columns and 'total_deaths' in df.columns:
    df['recovery_rate'] = ((df['total_cases'] - df['total_deaths']) / df['total_cases']) * 100
    df['recovery_rate'].fillna(0, inplace=True)  # Handle NaN values
    print("Recovery rate column created successfully!")
else:
    print(" 'total_cases' or 'total_deaths' column is missing!")

#Top 10 Countries by Recovery Rate
if 'recovery_rate' in df.columns and 'country' in df.columns:
    latest_date = df['date'].max()
    latest_data = df[df['date'] == latest_date]  # Get data for the latest available date
    top_recovery = latest_data.nlargest(10, 'recovery_rate')

    plt.figure(figsize=(12,6))
    # creating a horizontal bar chart
    sns.barplot(x='recovery_rate', y='country', data=top_recovery, palette='coolwarm')

    # adding labels and titles
    plt.xlabel("Recovery Rate (%)")
    plt.ylabel("Country")
    plt.title("Top 10 countries by recovery rate")

    # displaying the plot
    plt.show()
else:
    print(" 'recovery_rate' column not found.")


# save processed data
df.to_csv("covid_cleaned_data.csv", index=False)
print("Processed data saved as 'covid_cleaned_data.csv' ")