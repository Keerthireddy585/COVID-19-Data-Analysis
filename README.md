# COVID-19-Data-Analysis
This project presents an end-to-end analysis of the global COVID-19 pandemic using a publicly available dataset from "Our World in Data". It includes data extraction, cleaning, transformation, exploratory analysis, and insightful visualizations focused on case growth, recovery rates, and comparisons between countries.

## Project Objective
To extract, clean, analyze, and visualize COVID-19 data from a public dataset, uncover trends over time, and highlight key metrics such as total cases, deaths, and recovery rates across countries.

## Dataset
- **Source**: [Our World in Data - COVID-19] (https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv)
- **Size**: 100,000+ rows
- **Key Columns Used**: `date`, `country`, `total_cases`, `total_deaths`

## Tools & Technologies Used
- **Language**: Python
- **Libraries**: Pandas, Numpy, Matplotlib, Seaborn
- **Development Environment**: Visual Studio Code

## Data Cleaning & Preprocessing
- Loaded dataset directly from URL using `pandas.read_csv()`
- Converted `date` column to datetime format
- Handled missing values using `fillna(0)`
- Verified the presence of essential columns
- Exported cleaned dataset as `covid_cleaned_data.csv`

## Data Analysis & Key Insights

### 1. Trend Analysis: India
- Visualized **total cases** and **total deaths** in India over time
- Used line plots to show progression using `matplotlib` and `seaborn`

### 2. Top 10 Countries by Total Cases
- Filtered data for the most recent date
- Used `nlargest()` to identify countries with highest case counts

### 3. Recovery Rate Calculation
- Computed as:  
  ((total_cases - total_deaths) / total_cases) * 100
- Added a new column `recovery_rate`

### 4. Country-wise Comparison: India, UK, Germany
- Plotted total cases over time for all 3 countries
- Used `seaborn.lineplot()` with color-coded trends

### 5. Top 10 Countries by Recovery Rate
- Identified countries with highest recovery rates
- Visualized using horizontal bar plot (`seaborn.barplot()`)

## Output Files
- `covid_analysis.py` – Complete code for analysis and visualization
- `covid_cleaned_data.csv` – Cleaned and preprocessed data saved for further use

## Project Outcomes
- Built a clean, reproducible data analysis pipeline from scratch
- Strengthened data wrangling, analysis, and visualization skills
- Gained insights into global pandemic trends and country-wise recovery patterns












