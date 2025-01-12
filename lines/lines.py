import sys
import os

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")


    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check if the file name ends with .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, "r") as file:
            lines_of_code = 0

            for line in file:
                stripped_line = line.strip()

                # Ignore blank lines
                if stripped_line == "":
                    continue

                # Ignore comments
                if stripped_line.startswith("#"):
                    continue

                # Count lines of code
                lines_of_code += 1

        print(lines_of_code)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
