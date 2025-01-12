
import sys
import random
from pyfiglet import Figlet

def print_usage_and_exit():
    print("Usage: python figlet.py [-f <font>]")
    sys.exit(1)

def main():
    figlet = Figlet()

    # Check command-line arguments
    if len(sys.argv) == 2 and sys.argv[1] not in ['-f', '--font']:
        print_usage_and_exit()
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font']:
            print("Error: Invalid command-line arguments.")
            print_usage_and_exit()
        else:
            font_name = sys.argv[2]
            if font_name not in figlet.getFonts():
                print(f"Error: Font '{font_name}' not found.")
                sys.exit(1)
            figlet.setFont(font=font_name)

    # Prompt user for input text
    text = input("INPUT: ")

    # Output text in the desired font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()


