'''
Q3preprocess.py
Author(s): Hamza Memon (1235100)
Project: Milestone IV Program Code
Date of Last Update: April 4th, 2024

Functional Summary

This program reads through 2 CSV files, one containing data regarding labour force and the other wages by education level. 
In the command line, the program asks the user for a specific year and province. 
Using this input, the program filters through both csv files and outputs all the data that is within the inputted time frame by the user, while also ensuring that no more than 50 rows per dataset and 5 rows per education level are printed.

Commandline Parameters: 5
argv[0] = program file
argv[1] = Labour force file (data-2015-2019.csv)
argv[2] = Wages file (wages.csv)
argv[3] = year
argv[4] = province

'''
import csv
import sys

def main(argv):
    if len(argv) != 5:
        print("Usage: python {} data-2015-2019.csv wages.csv <year> <province>".format(argv[0]))
        sys.exit(1)

    # command line arguments
    labor_force_path = argv[1]
    wages_path = argv[2]
    year = argv[3]
    province = argv[4]

    # validating input
    if not year.isdigit():
        print("Year must be a four-digit number.")
        sys.exit(1)

    try:
        # processing the labour force dataset
        with open(labor_force_path, newline='', encoding="utf-8-sig") as labor_file:
            labor_reader = csv.DictReader(labor_file)
            print("\nLabour Force Data:")
            print(",".join(labor_reader.fieldnames))

            education_counts_labor = {}
            row_count_labor = 0

            for row in labor_reader:
                if row_count_labor >= 50:
                    break  # Break out of the loop if 50 rows have been printed

                if year in row['Timeseries'] and province.upper() == row['Prov'].upper().strip():
                    education_level = row['Education'].strip()
                    education_counts_labor[education_level] = education_counts_labor.get(education_level, 0) + 1
                    
                    if education_counts_labor[education_level] <= 5:
                        print(','.join([row[fieldname].strip() for fieldname in labor_reader.fieldnames]))
                        row_count_labor += 1

        # processing the wages dataset
        with open(wages_path, newline='', encoding="utf-8-sig") as wages_file:
            wages_reader = csv.DictReader(wages_file)
            print("\nWages Data:")
            print(",".join(wages_reader.fieldnames))

            education_counts_wages = {}
            row_count_wages = 0

            for row in wages_reader:
                if row_count_wages >= 50:
                    break  # break out of the loop if 50 rows have been printed

                if year == row['YEAR'] and province.upper() == row['Geography'].upper().strip():
                    education_level = row['Education level'].strip()
                    education_counts_wages[education_level] = education_counts_wages.get(education_level, 0) + 1
                    
                    if education_counts_wages[education_level] <= 5:
                        print(','.join([row[fieldname].strip() for fieldname in wages_reader.fieldnames]))
                        row_count_wages += 1

    except IOError as err:
        print(f"Unable to open file: {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)
