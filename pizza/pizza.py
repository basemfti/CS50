import csv
import sys
from tabulate import tabulate

def main():
    
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]


    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try to open the file
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            headers = next(reader)  # Get the headers from the first row
            data = [row for row in reader]
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Use tabulate to format the table
    table = tabulate(data, headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
