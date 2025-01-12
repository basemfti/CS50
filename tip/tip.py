def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
      return float(d.replace('$',''))

# Example usage:
#amount = "$50.00"
#amount_float = dollars_to_float(amount)
#print(amount_float)

def percent_to_float(p):
    return float(p.strip('%')) / 100


main()
