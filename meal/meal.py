
def main():

    time_input = input("what time is it? ")
    time = convert(time_input)

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")

def convert(time):

    #Converts time from 24-hour format to hours as a float.

    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
