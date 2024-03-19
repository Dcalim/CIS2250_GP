import csv
import sys


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