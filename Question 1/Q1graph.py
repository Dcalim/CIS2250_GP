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
    fileName = argv[1]                  #Datafile
    referenceDates = argv[2].split('-') # Date(s), can be a range like "2015-2018"
    provinces = argv[3].split(',')    # Provinces, split into a list
    educationLevel = argv[4]            #Education Level

    #Error Checking (Ensuring the user inputted valid inputs)

    #Error checking for referenceDates
    valid_years = {'2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'}

    for year in referenceDates:
        if year not in valid_years:
            print("Error: Invalid date. Please enter the date in years (ex. 2005) and ensure it is within the range 2015-2023")
            sys.exit(1)
    
    #Error Checking for provinces
    valid_provinces = {
    'Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia','New Brunswick', 'Quebec', 'Ontario', 'Manitoba'
    ,'Saskatchewan','Alberta', 'British Columbia', 'Yukon', 'Northwest Territories','Nunavut', 'Canada'}

    for prov in provinces:
        if prov not in valid_provinces:
            print("Error: Invalid location. Please ensure the location is valid from the provided list")
            sys.exit(1)
    
    #Error Checking for education level
    valid_education_levels = {
    'Full-time', 'Part-time', 'No minimum level of education required','High school diploma or equivalent', 'Bachelor\'s degree',
    'University certificate, diploma or degree above the bachelor\'s level'}

    if educationLevel not in valid_education_levels:
        print("Error: Invalid education level. Please ensure the education level is valid from the provided list")
        sys.exit(1)



    #Attempting to open the CSV file
    try:
        nameFile = open(fileName, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open file '{}' : {}".format(fileName, err), file=sys.stderr)
        sys.exit(1)

    #Creating a CSV reader to read the file
    fileReader = csv.reader(nameFile)

    # opening an output csv file 
    output_file = open('question1.csv','w', newline ='')
    csvwriter = csv.writer(output_file)

    #Reading and printing headers
    headers = next(fileReader)
    print("{},{},{},{},{},{}".format(headers[0], headers[1], headers[3], headers[4], headers[5], headers[12]))
    fields = [headers[0], headers[1], headers[3], headers[4], headers[5], headers[12]]
    csvwriter.writerow(fields)

    # Converting referenceDates to integer for comparison
    startYear = int(referenceDates[0])

    #Setting an end year value if there are more than one years inputted, else the value is set to startYear
    endYear = int(referenceDates[-1]) if len(referenceDates) > 1 else startYear

    # Going through each row in the file and checking conditions 
    for row in fileReader:
        # Extracting the year part from the 'REF_DATE' field
        year_part = int(row[0].split("-")[0])

        # Check if the province in the row is one of the user-specified provinces
        if startYear <= year_part <= endYear and row[1] in provinces and row[3] == "Software engineers and designers [2173]" and row[4] == educationLevel and row[5] == "Job vacancies":
            # If 'VALUE' is empty, prints a 0
            if row[12] == "":
                print("{},{},{},{},{},0".format(row[0], row[1], row[3], row[4], row[5]))
                fields = [row[0], row[1], row[3], row[4], row[5], '0']
                csvwriter.writerow(fields)
            else:
                # Printing the result of 'VALUE'
                print("{},{},{},{},{},{}".format(row[0], row[1], row[3], row[4], row[5], row[12]))
                fields = [row[0], row[1], row[3], row[4], row[5], row[12]]
                csvwriter.writerow(fields)

    # Close the file after writing
    output_file.close()


    

main(sys.argv)
