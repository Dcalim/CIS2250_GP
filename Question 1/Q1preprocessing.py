'''
Q1preprocessing.py
Author(s): Adam Mohamed (1264605)
Project: Milestone IV Program Code
Date of Last Update: April 4th, 2024

Function Summary:
The program is given 4 command line arguements from the user, the datafile, date, province, and education level. The program creates a CSV reader
for the datafile, and using the given information from the user, locates the data the fits the requirements. The program then prints all the 
information that fits the requirements of the command line arugements. 

Command Line Parameters: 4
argv[0] = Program
argv[1] = MetaData (Datafile)
argv[2] = Date 
argv[3] = Province
argv[4] = Education Level

'''

import sys
import csv

def main(argv):

    #Checking if there are the correct number of command line arguements
    if len(argv) != 5:
        print("Usage: {} <fileName> <referenceDate> <geography> <educationLevel>".format(argv[0]))
        sys.exit(1)

    #Command line arguments
    fileName = argv[1]          #Datafile
    referenceDate = argv[2]     #Date (In years)
    geography = argv[3]         #Province
    educationLevel = argv[4]    #Education Level

    #Attempting to open the CSV file
    try:
        nameFile = open(fileName, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open file '{}' : {}".format(fileName, err), file=sys.stderr)
        sys.exit(1)

    #Creating a CSV reader to read the file
    fileReader = csv.reader(nameFile)

    # opening an output file 
    Small_file = open('question1.csv','w', newline ='')
    csvwriter = csv.writer(Small_file)

    #Reading and printing headers
    headers = next(fileReader)
    print("{},{},{},{},{},{}".format(headers[0], headers[1], headers[3], headers[4], headers[5], headers[12]))
    fields = [headers[0], headers[1], headers[3], headers[4], headers[5], headers[12]]
    csvwriter.writerow(fields)

    #Going through each row in the file and checking conditions 
    for row in fileReader:

        #Extracting the year part from the 'REF_DATE' field
        year_part = row[0].split("-")[0]

        #Locating the data that fits the user's requirements
        if(year_part == referenceDate and row[1] == geography and row[3] == "Software engineers and designers [2173]" and row[4] == educationLevel and row[5] == "Job vacancies"):
            #If 'VALUE' is empty, prints a 0
            if row[12] == "":
                 print("{},{},{},{},{},0".format(row[0], row[1], row[3], row[4], row[5]))
                 fields = [row[0], row[1], row[3], row[4], row[5]] 
                 csvwriter.writerow(fields)
            else:
                #Printing the result of 'VALUE'
                print("{},{},{},{},{},{}".format(row[0], row[1], row[3], row[4], row[5], row[12]))
                fields = [row[0], row[1], row[3], row[4], row[5], row[12]] 
                csvwriter.writerow(fields)

    

main(sys.argv)
