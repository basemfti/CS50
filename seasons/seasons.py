from datetime import date
import inflect
import re
import sys


p= inflect.engine()



def main():

    birth_date=input("birth date: ")

    try:
        year, month,day= check_birthday(birth_date)

    except:
        sys.exit("Invalid date")


    date_of_birth=date(int(year),int(month),int(day))
    date_of_today=date.today()
    dif_date=date_of_today-date_of_birth
    minites=dif_date.days * 24 * 60
    words = p.number_to_words(minites,andword="")

    print(words.capitalize()+" minutes")


def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$" ,birth_date):
        year,month,day=birth_date.split("-")
    return year,month,day


if __name__ == "__main__":
    main()
