import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
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

    df = pd.read_csv(fileName)

    if ((df['REF_DATE'].str[:4] == year) & (df['GEO'] == province)).any():
        csvYear = df[(df['REF_DATE'].str[:4] == year) & (df['GEO'] == province)]['REF_DATE']
        csvValue = df[(df['REF_DATE'].str[:4] == year) & (df['GEO'] == province)]['VALUES'] 
        print("Printing csvYear\n")
        print(csvYear)
        print("Finished Printing csvYear\n\n")

        print("Printing csvValues")
        print(csvValue)
        print("Done Printing csvValues\n")

        plt.plot(csvYear, csvValue)
        plt.show()

    else:
        print("No data found for the specified province and year.")

main(sys.argv)