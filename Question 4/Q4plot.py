'''
Q4plot.py
Author(s): Hamza Memon (1235100)
Project: Milestone IV Program Code
Date of Last Update: April 4th, 2024

Functional Summary

This program reads through a CSV input file (umployment_duration.csv) and then uses the month + year inputted by the user in the command line. 
Using this input, the program filters through the specificed time frame and plots the data using a bar graph 

Commandline Parameters: 2
argv[0] = program file
argv[1] = CSV data file (umployment_duration.csv)
argv[2] = month + year (eg. Mar2015)

'''

import pandas as pd  # for data analysis
import matplotlib.pyplot as plt  # for visualizations
import sys  

def plot_unemployment(csv_file, selected_month):
    
    # pandas reads the CSV and converts it into a table like structure 
    unemployment_data = pd.read_csv(csv_file)

    # filter the structure to only include rows for a specific month.
    data_selected_month = unemployment_data[unemployment_data['MONTH'] == selected_month]

    # define the desired order of the age groups.
    age_group_order = ['15-19', '20-24', '25-44', '45-54', '55-64', '65 years and over']

    # ensures that the 'AGE GROUP' column in data_selected_month is treated as categorical data
    # ordered as true indicates that the categorical variable has a logical order 
    data_selected_month['AGE GROUP'] = pd.Categorical(data_selected_month['AGE GROUP'], categories=age_group_order, ordered=True)

    # selected month is organzied by age group, collecting rows that have the same value in specified columns
    # sum function collects all the numerical data in a specific column
    # index is reset to move to the next column
    # dropna function ensures that any missing values that do not match with the age group are dropped
    grouped_data_sorted = data_selected_month.groupby('AGE GROUP').sum().reset_index().dropna(subset=['AGE GROUP'])

    # creates a single plot, specifying the figure as 15x8
    figure, axes = plt.subplots(figsize=(15, 8))
    bar_width = 0.4  

    # accessing age group columns from the sorted data 
    age_groups = grouped_data_sorted['AGE GROUP']

    # finding the number of age groups and turning it into a list of positions
    positions = list(range(len(age_groups)))

    # creating a bar chart on the specificed axes 
    # for each position, bar width is subtracted to ensure the male and female bars do not overlap
    axes.bar([p - bar_width/2 for p in positions], grouped_data_sorted['Male'], bar_width, label='Male', color='blue')
    axes.bar([p + bar_width/2 for p in positions], grouped_data_sorted['Female'], bar_width, label='Female', color='pink')

    # setting the x axis, y axis, and title for the plot
    axes.set_xlabel('Age Group', fontweight='bold')
    axes.set_ylabel('Sum of Unemployment Figures in ' + selected_month)
    axes.set_title('Sum of Unemployment Figures by Age Group and Gender in Ontario - ' + selected_month)

    axes.set_xticks(positions)
    axes.set_xticklabels(age_groups, rotation=0)
    axes.legend()

    plt.show()

    # Check if exactly three arguments have been provided (including the script name).
    if len(sys.argv) != 3:
        print("Usage: python Q4unemploymentData.py umployment_duration.csv 'MonthYear'")
        sys.exit(1)
    
csv_file_path = sys.argv[1]
month_year = sys.argv[2]
# Call the plot_unemployment function with the provided CSV file path and month + year to generate the plot.
plot_unemployment(csv_file_path, month_year)
