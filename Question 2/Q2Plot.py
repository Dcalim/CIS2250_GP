import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import pyplot as plt
import sys

# Q2Plot.py
# Author(s): Dion Calim (1275684)
# Project: Group Assignment Project
# Date of Last Update: April 1, 2024

# IMPORTANT
# Please run preProcessingQ2.py if you have not done so yet for most accurate and up to date data

# Functional Summary
# This python file will plot average monthly earnings for all employees in a specfic province or territory in a specific year
# The user will have a opportunity to select a province and year in the command line

# Command line parameters: 4
# argv[0] = program file (plotQ2.py)
# argv[1] = pre processed csv file (Question2Processed.csv)
# argv[2] = province (ex, Newfoundland and Labrador)
# argv[3] = year (ex, 2023)


def main(argv):
    
    #error handling 
    if len(argv) != 4:
        print("Usage: {} <fileName>".format(argv[0]))
        sys.exit(1)

    #command line arguments 
    fileName = argv[1]
    province = argv[2]
    year = argv[3]

    months = ["January", "Februrary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    #data fields read from csv file
    df = pd.read_csv(fileName)

    # Runs if any data fields in csv file matches the province inputted by user
    if ((df['GEO'] == province)).any():
        
        # Runs if any data fields in csv file matches the year inputted by user
        if((df['REF_DATE'].str[:4] == year)).any():
            csvYear = df[(df['REF_DATE'].str[:4] == year) & (df['GEO'] == province)]['REF_DATE']
            csvValue = df[(df['REF_DATE'].str[:4] == year) & (df['GEO'] == province)]['VALUES'] 

            plt.title(province + " average monthly earning in " + year, fontweight='bold')
            plt.xlabel("Months", fontweight='bold')
            plt.ylabel("Average Earning in Dollars", fontweight='bold')
            plt.plot(months, csvValue)
    
            # Showing plot on full seperate screen
            manager = plt.get_current_fig_manager()
            manager.full_screen_toggle()
            plt.show()
        
        # Runs if it cannot find the year inputted by user
        else:
            print("Could not find any data for that year.")

    
    # Runs if it cannot find the province inputted by user
    else:
        print("No data found for the specified province, please ensure that the province is beginning with a capital.")
        sys.exit()

main(sys.argv)