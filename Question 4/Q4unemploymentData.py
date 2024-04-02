'''
Q4unemploymentData.py
Author(s): Hamza Memon (1235100)
Project: Milestone IV Program Code
Date of Last Update: April 4th, 2024

Functional Summary

This program reads through a CSV input file (umployment_duration.csv) and asks the user to enter a specific month and year. 
Using this input, the program filters through the csv file and outputs all the data that is within the inputted time frame by the user. 

Commandline Parameters: 2
argv[0] = program file
argv[1] = CSV data file (umployment_duration.csv)
argv[2] = month + year (eg. Mar2015)

'''
import csv  
import sys  



def main(argv):
    # ensure the correct number of command-line arguments is provided
    if len(argv) != 3:
        # if not, print the correct usage of the script and exit with an error
        print("Usage: python {} input_file.csv 'MonthYear'".format(argv[0]))
        sys.exit(1)  

    # command line argument
    input_file_path = argv[1]
    month_year = argv[2]

    try:
        with open(input_file_path, newline='', encoding="utf-8-sig") as csv_file:
            # CSV DictReader to read the CSV file
            file_reader = csv.DictReader(csv_file)

            # print the column headers retrieved from the CSV file
            # joins all the elements from the iterable and creates a string. Returns it as output
            print(",".join(file_reader.fieldnames))

            # loop through each row in the CSV file
            for row in file_reader:
                # check if the row's 'MONTH' column matches the user's input
                if row['MONTH'] == month_year:
                    # if a match is found, print the relevant details of the row
                    print("{},{},{},{},{},{},{}".format(
                        row['MONTH'], row['GEOGRAPHY'], row['DURATION'], 
                        row['AGE GROUP'], row['Both sexes'], row['Male'], row['Female']))

    # catch and handle IOErrors, for example, if the file cannot be found or opened
    except IOError as err:
        print("Unable to open the file '{}' : {}".format(input_file_path, err), file=sys.stderr)
        sys.exit(1)  

main(sys.argv) 
