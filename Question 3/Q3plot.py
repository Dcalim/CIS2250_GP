'''
Q3plot.py
Author(s): Hamza Memon (1235100)
Project: Milestone IV Program Code
Date of Last Update: April 4th, 2024

Functional Summary

This program reads through 2 CSV files, one containing labour force data and the other containing wages by education level.
It filters the data by the specified year and province, then outputs two bar graphs in one figure:
the first bar graph shows the total employment by education level,
and the second bar graph shows the average weekly wages by education level.

Commandline Parameters: 4
argv[0] = program file
argv[1] = Labour force file (data-2015-2019.csv)
argv[2] = Wages file (wages.csv)
argv[3] = province
argv[4] = year

'''
import pandas as pd
import matplotlib.pyplot as plt
import sys
import re

# removes any text within parentheses, including the parentheses during the final output
def remove_parenthesis(s):
    return re.sub(r"\s*\([^)]*\)", "", s)

# plotting employment and wages data in bar graphs
def plot_employment_and_wages(labour_csv, wages_csv, province, year):
    labour_data = pd.read_csv(labour_csv)
    wages_data = pd.read_csv(wages_csv)
    
    # filtering out specific education levels for the labour force dataset
    required_levels_labor = [
        '  No PSE  (0,1,2,3,4)',
        '    Some high school,  (1+2)', '    High school, (3)',
        '    Some post-secondary, (4)', 'Post-secondary education (5 to 9), ',
        '  University degree (8+9)', '     Bachelor degree (8)',
        '     Above Bachelor\'s degree (9)"'
    ]
    
    # filtering out specific education levels for the wages dataset
    required_levels_wages = ['   Some high school',
    '   High school graduate' '   Some post-secondary'
    '   Post-secondary certificate or diploma',
    '    Trade certificate or diploma', '    Community college, CEGEP',
    '   University degree', "      Bachelor's degree",
    'PSE  (5,6,7,8,9))', 'No PSE  (0,1,2,3,4)'
    ] 

    # filter the data for required education levels and by province and year
    labour_filtered = labour_data[
        (labour_data['Prov'] == province) &
        (labour_data['Timeseries'].str.contains(year)) &
        (labour_data['Education'].isin(required_levels_labor)) 
    ]
    
    # filter the wages data by province, year, and wage type
    wages_filtered = wages_data[
        (wages_data['Geography'] == province) &
        (wages_data['YEAR'].astype(str) == year) &
        (wages_data['Education level'].isin(required_levels_wages)) &
        (wages_data['Wages'] == "Average weekly wage rate")
    ]
 
    # group and sum the total employment for each education level
    labour_stats = labour_filtered.groupby('Education')['Total'].sum()

    # group and calculate the mean of wages for each education level
    wage_stats = wages_filtered.groupby('Education level')['Both Sexes'].mean()

    # removing parentheses 
    labour_stats.index = labour_stats.index.map(remove_parenthesis)
    wage_stats.index = wage_stats.index.map(remove_parenthesis)

    # create subplots
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

    # plotting the employment data
    labour_stats.plot(kind='bar', ax=axes[0], color='skyblue')
    axes[0].set_title(f'Total Employment by Education Level in {province} - {year}')
    axes[0].set_ylabel('Total Employment')
    
    # plotting the wages data
    wage_stats.plot(kind='bar', ax=axes[1], color='lightgreen')
    axes[1].set_title(f'Average Weekly Wages by Education Level in {province} - {year}')
    axes[1].set_ylabel('Average Weekly Wages (CAD)')
    
    # setting the x-labels
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45)
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <labour_csv> <wages_csv> <province> <year>")
        sys.exit(1)
    
    # command line arguments
    labour_csv = sys.argv[1]
    wages_csv = sys.argv[2]
    province = sys.argv[3]
    year = sys.argv[4]
    
    plot_employment_and_wages(labour_csv, wages_csv, province, year)

