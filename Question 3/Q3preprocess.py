'''
Q3preprocess.py
Author(s): Hamza Memon (1235100)
Project: Milestone IV Program Code
Date of Last Update: April 4th, 2024

Functional Summary

This program reads through 2 CSV files, one containing data regarding labour force and the other wages by education level. 
In the command line, the program asks the user for a specific year and province. 
Using this input, the program filters through both csv files and outputs all the data that is within the inputted time frame by the user, while also ensuring that no more than 50 rows per dataset and 5 rows per education level are printed.

Commandline Parameters: 4
argv[0] = program file
argv[1] = Labour force file (data-2015-2019.csv)
argv[2] = Wages file (wages.csv)
argv[3] = province
argv[4] = year

'''
import csv
import sys

def main(argv):
    if len(argv) != 5:
        print("Usage: python {} data-2015-2019.csv wages.csv <province> <year>".format(argv[0]))
        sys.exit(1)

    # command line arguments
    labour_force_path = argv[1]
    wages_path = argv[2]
    province = argv[3]
    year = argv[4]

    # validating input
    if not year.isdigit():
        print("Year must be a four-digit number.")
        sys.exit(1)

    try:
        # processing the labour force dataset
        with open(labour_force_path, newline='', encoding="utf-8-sig") as labor_file:
            # creates a dictionary reader for the CSV, allowing for data to be accessed by column names
            labour_reader = csv.DictReader(labor_file)
            print("\nLabour Force Data:")
            print(",".join(labour_reader.fieldnames))

            # to count the number of rows per education level
            education_counts_labour = {}

            # tracks the total number of rows printed
            row_count_labour = 0

            # iterating through each row in the labour force data file
            for row in labour_reader:
                # breaking if 50 rows have been printed
                if row_count_labour >= 50:
                    break  

                # check to see if the row matches the specified year and province
                # converts the 'Prov' field to uppercase and removes leading/trailing whitespace
                if year in row['Timeseries'] and province.upper() == row['Prov'].upper().strip():
                    # updates the count of rows for the current education level
                    education_level = row['Education'].strip()
                    education_counts_labour[education_level] = education_counts_labour.get(education_level, 0) + 1
                    
                    # limiting the number of rows printed per education level to 5
                    if education_counts_labour[education_level] <= 5:
                        print(','.join([row[fieldname].strip() for fieldname in labour_reader.fieldnames]))
                        row_count_labour += 1

        # processing the wages dataset
        with open(wages_path, newline='', encoding="utf-8-sig") as wages_file:
            wages_reader = csv.DictReader(wages_file)
            print("\nWages Data:")
            print(",".join(wages_reader.fieldnames))

            # to count the number of rows per education level
            education_counts_wages = {}

            # tracks the total number of rows printed
            row_count_wages = 0

            for row in wages_reader:
                if row_count_wages >= 50:
                    break  # break out of the loop if 50 rows have been printed

                # check to see if the row matches the specified year and province
                if year == row['YEAR'] and province.upper() == row['Geography'].upper().strip():
                    education_level = row['Education level'].strip()
                    education_counts_wages[education_level] = education_counts_wages.get(education_level, 0) + 1
                    
                    # limiting the number of rows printed per education level to 5
                    if education_counts_wages[education_level] <= 5:
                        print(','.join([row[fieldname].strip() for fieldname in wages_reader.fieldnames]))
                        row_count_wages += 1

    except IOError as err:
        print(f"Unable to open file: {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)
