months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def is_valid_date(date_str):
    try:
        if '/' in date_str:
            parts = date_str.split('/')
            if len(parts) != 3:
                return False
            month, day, year = map(int, parts)
            if month < 1 or month > 12 or day < 1 or day > 31 or year < 0:
                return False
            return True
        else:
            parts = date_str.replace(',', '').split()  # Remove comma before splitting
            month, day, year = parts[0], int(parts[1]), int(parts[2])
            if month not in months or day < 1 or day > 31 or year < 0:
                return False
            return True
    except ValueError:
        return False



def convert_to_iso(date_str):

    if '/' in date_str:
        month, day, year = map(int, date_str.split('/'))
        return f"{year:04d}-{month:02d}-{day:02d}"
    else:

        ch = date_str.replace(',', '') # Remove comma before splitting

        month, day,year = ch.split()

        for i, month_name in enumerate(months, start=1):
            if month_name == month:
             return f"{int(year):04d}-{int(i):02d}-{int(day):02d}"



def main():
    while True:
        date_str = input("Enter a date (in month-day-year format): ")
        if is_valid_date(date_str):
            iso_date = convert_to_iso(date_str)
            print(iso_date)
            break
        else:
            print("Invalid date. Please try again.")

if __name__ == "__main__":
    main()

