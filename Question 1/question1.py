import sys
import csv
import pandas as pd

def main(argv):

    # Error handling for command line arguments
    if len(argv) != 5:
        print("Usage: {} <fileName> <referenceDate> <geography> <educationLevel>".format(argv[0]))
        sys.exit(1)

    # Command line arguments
    fileName = argv[1]
    referenceDate = argv[2]
    geography = argv[3].split(',')  # Allows for multiple provinces/territories
    educationLevel = argv[4]

    # Opening the CSV file
    try:
        nameFile = open(fileName, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open file '{}' : {}".format(fileName, err), file=sys.stderr)
        sys.exit(1)

    fileReader = csv.reader(nameFile)

    # Reading and printing headers
    headers = next(fileReader)
    print("{},{},{},{},{},{}".format(headers[0], headers[1], headers[3], headers[4], headers[5], headers[12]))

    # Iterating through each row in the file and checking conditions
    for row in fileReader:
        if (row[0] == referenceDate and row[1] in geography and row[4] == educationLevel and row[5] == "Job vacancies"):
            # Printing results when value is not given
            if row[12] == "":
                print("{},{},{},{},{},0".format(row[0], row[1], row[3], row[4], row[5]))
            else:
                # Printing results when value is given
                print("{},{},{},{},{},{}".format(row[0], row[1], row[3], row[4], row[5], row[12]))
    

    main(sys.argv)
