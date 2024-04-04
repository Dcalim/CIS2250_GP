'''
Q1graph.py
Author(s): Adam Mohamed (1264605)
Project: Milestone IV Program Code
Date of Last Update: April 4th, 2024

Function Summary:
The program is given 1 command like arguement from the user, the processed data within the newly created CSV file. The program takes
the data and using pandas reads the csv file into a dataframe. The program then checks the dataframe by printing out the data to the user. 
The program then pivots the dataframe, reshaping it for graphing. The program then graphs the data into a bar graph, where the y-axis is 
the number of job vacancies, the x-axis is the date, and each bar represents the province or territory as shown within the legend. 

Command Line Parameters: 1
argv[0] = Program
argv[1] = datafile.csv (Datafile)

'''

import sys
import pandas as pd
import matplotlib.pyplot as plt

def main(argv):
    #Checking if there are the correct number of command line arguements
    if len(argv) < 2:
        print("Usage: {} <CSV_File>".format(argv[0]))
        sys.exit(1)
    
    #Command line argument
    filename = argv[1]  #CSV datafile

    # Reading the CSV file into a pandas DataFrame
    df = pd.read_csv(filename)

    # Checking the first few rows of the DataFrame to inspect the data
    print(df.head())

    # Pivot the DataFrame to reshape it for plotting, rearranging data based on columns
    pivot_df = df.pivot(index='REF_DATE', columns='GEO', values='VALUE')

    # Plotting a bar graph for each province side by side based on the pivoted DataFrame
    pivot_df.plot(kind='bar', title="Job Vacancies Over Time by Province")

    # Customize the plot
    plt.xlabel('Date')                                  #Set label for x-axis
    plt.ylabel('Number of Vacancies')                   #Set label for y-axis
    plt.xticks(rotation=45)                             #Rotate the x-axis labels for better readability
    plt.legend(title="Province(s) and/or Territories")  #Add legend with a title
    plt.title("Job Vacancies Over Time by Province")    #Add title to the plot
    plt.tight_layout()                                  #Adjust layout to prevent labels from being cut off

    #Displaying the plot to the user
    plt.show()

main(sys.argv)
