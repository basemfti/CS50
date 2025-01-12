import re
import sys



def main():
    print(validate(input("IPv4 Address: ")))



def validate(ch):
   pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

   if re.match(pattern, ch):

        parts = ch.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return True
   return False




if  __name__=="__main__":

 main()
