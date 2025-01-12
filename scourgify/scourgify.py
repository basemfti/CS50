import csv
import sys

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Too many command-line arguments or Too few command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Open the input CSV file for reading
        with open(input_file, newline='') as infile:
            reader = csv.DictReader(infile)

            # Prepare the output CSV file for writing
            with open(output_file, mode='w', newline='') as outfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                # Process each row in the input file
                for row in reader:
                    name = row['name']
                    house = row['house']

                    # Split the name into first and last
                    last, first = name.split(', ')

                    # Write the cleaned data to the output file
                    writer.writerow({'first': first, 'last': last, 'house': house})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
