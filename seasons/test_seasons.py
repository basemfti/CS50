
from seasons import check_birthday
import pytest


def main():



  def test():

    assert check_birthday('1998-07-03') == ("1998","07","03")
    assert check_birthday('1998-7-3') == None
    assert check_birthday('jule 08,2023')==None

if __name__ == "__main__":
    main()




