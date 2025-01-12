from cs50 import get_float

def main():
    # Get the input and convert to cents
    cents = get_float("change: ")

    while cents <= 0:  # Validate positive input
        cents = get_float("change: ")

    cents = round(cents * 100)  # Convert dollars to cents and round

    # Calculate coins
    quarters = calculate_quarters(cents)
    cents -= quarters * 25  # Subtract quarters value

    dimes = calculate_dimes(cents)
    cents -= dimes * 10  # Subtract dimes value

    nickels = calculate_nickels(cents)
    cents -= nickels * 5  # Subtract nickels value

    # Remaining cents are pennies
    pennies = cents

    # Output the total number of coins
    print(f"{quarters + dimes + nickels + pennies}")

def calculate_quarters(cents):
    quarters = 0
    while cents >= 25:
        quarters += 1
        cents -= 25
    return quarters

def calculate_dimes(cents):
    dimes = 0
    while cents >= 10:
        dimes += 1
        cents -= 10
    return dimes

def calculate_nickels(cents):
    nickels = 0
    while cents >= 5:
        nickels += 1
        cents -= 5
    return nickels

if __name__ == "__main__":
    main()
