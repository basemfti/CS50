import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py <database.csv> <sequence.txt>")
        sys.exit(1)

    # Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], encoding="utf-8") as f:
        read_data = f.read()

    # Find longest match of each STR in DNA sequence
    str_list = list(reader.fieldnames)  # Get STR names from database headers
    str_list.remove('name')  # Remove the name field
    dna = {}
    for str_seq in str_list:
        dna[str_seq] = longest_match(read_data, str_seq)

    # Check database for matching profiles
    for person in rows:
        match = True
        for str_seq in str_list:
            if int(person[str_seq]) != dna[str_seq]:
                match = False
                break
        if match:
            print(person['name'])
            sys.exit(0)

    # If no match found
    print("No match")
    sys.exit(1)


def longest_match(sequence, subsequence):


    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
