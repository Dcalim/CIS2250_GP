import csv
import sys

# preProcessingQ2.py
# Author(s): Dion Calim (1275684)
# Project: Group Assignment Project
# Date of Last Update: April 1, 2024

# IMPORTANT
# ******* Downloading most updated file *******
# 1. Go to https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410022301 
# 1.1 If link does not work: go to https://www150.statcan.gc.ca/n1/en/type/data?MM=1 or Stats Canada → data → search 
#     “Employment and average weekly earnings (including overtime) for all employees by province and territory, monthly, seasonally adjusted” 
#     or “14-10-0223-01”
# 2. Click Download Options
# 3. Click CSV: Download entire table

# Functional Summary
# This python file will pre process the csv file regarding Employment and average weekly earnings (including overtime) for all employees by province 
# and territory. The python file will grab information regarding year, location, industry and average weekly earning values and write them to a seperate
# csv file called "Question2Processed.csv"

# Command line parameters: 2
# argv[0] = program file (preProcessingQ2.py)
# argv[1] = full average weekly earning file (csv file name from downloading steps above)

def main(argv):
    month = 13
    income = []
    expectedYear = 0
    
    #error handling 
    if len(argv) != 2:
        print("Usage: {} <fileName>".format(argv[0]))
        sys.exit(1)

    #command line arguments 
    fileName = argv[1]

    
    # Opening the csv file
    try:
        file = open(fileName, encoding="utf-8-sig")
        outFile = open("Question2Processed.csv", 'w', newline='')

    #error handling
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(fileName, err), file=sys.stderr)
        sys.exit(1)

    # Creating file reader and file writer
    fileReader = csv.reader(file)
    csvWriter = csv.writer(outFile)

    # Writing Headers to file
    fields = ["REF_DATE", "GEO", "North American Industry Classification System (NAICS)", "UOM", "VALUES"]
    csvWriter.writerow(fields)

    # Writing average weekly earnings to file
    for row in fileReader:
        if row[4] == "Industrial aggregate excluding unclassified businesses [11-91N]" and row[3] == "Average weekly earnings including overtime for all employees":
            data = [row[0], row[1], row[3], row[4], row[11]]
            csvWriter.writerow(data)

                
    
main(sys.argv)