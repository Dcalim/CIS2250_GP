import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import pyplot as plt
import sys

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

    # Runs if any data fields in csv file matches year and province inputted by user
    if ((df['REF_DATE'].str[:4] == year) & (df['GEO'] == province)).any():
        csvYear = df[(df['REF_DATE'].str[:4] == year) & (df['GEO'] == province)]['REF_DATE']
        csvValue = df[(df['REF_DATE'].str[:4] == year) & (df['GEO'] == province)]['VALUES'] 
        print("Printing csvYear\n")
        print(csvYear)
        print("Finished Printing csvYear\n\n")

        print("Printing csvValues")
        print(csvValue)
        print("Done Printing csvValues\n")

        plt.title(province + " average monthly earning in " + year)
        plt.xlabel("Months")
        plt.ylabel("Average Earning in Dollars")
        plt.plot(months, csvValue)
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        plt.show()
    
    # Runs if it cannot find any date fields that match the year or province inputted by user
    else:
        print("No data found for the specified province and year.")
        sys.exit()

main(sys.argv)