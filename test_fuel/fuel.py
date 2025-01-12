def main():
    while True:
        try:
            fraction = input("Fraction: ")

            print(gauge(convert(fraction)))
            break
        except (ValueError,ZeroDivisionError):
            continue


def convert(fraction):
            a,b = fraction.split("/")
            f = int(a) / int(b)
            if int(a) <= int(b) and int(b) != 0 and f <= 1:
                percentage = int(round(f * 100))
                return percentage
            else:
                raise (ZeroDivisionError,ValueError)


def gauge(percentage):
    Z = int(percentage)
    if Z <= 1:
        return "E"
    elif Z >= 99:
        return "F"
    else:
        return f"{Z}%"


if __name__ == "__main__":
    main()
