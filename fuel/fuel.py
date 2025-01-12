def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            if percentage is not None:
                print (gauge(percentage))
                print(percentage)
                break
        except ValueError:
            print("Invalid input. Please enter again.")

def convert(fraction):
    numerator, denominator = map(int, fraction.split('/'))
    if denominator == 0 or numerator > denominator:
        raise ValueError("Invalid fraction.")
    else:
        return (numerator / denominator) * 100

def gauge(percentage):
    try:
        if percentage <= 1:
            return 'F'
        elif percentage >= 99:
            return 'E'
        else:
            return f"{round(percentage)}%"
    except (ValueError, ZeroDivisionError):
        return None

if __name__ == "__main__":
    main()
