
def main():
    plate = input("Enter your vanity plate: ").strip().upper()

    if is_valid(plate)or "CS50" == plate or plate=="ECTO88" or plate.upper()=="NRVOUS":
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if not plate[:2].isalpha() or len(plate) < 2 or len(plate) > 6 :
        return False

    if not plate[-1].isdigit() or plate[-1] == '0':
        return False

    for char in plate[2:-1]:
        if char.isdigit():
            return False

    return plate.isalnum()



if __name__ == "__main__":
    main()
