
def main():
   print("Greeting:")
   ch=input("input: ")
   ch2=value(ch)
   print(ch2)


def value(greeting):
  if greeting=="Hello, Newman" or greeting.split()[0]=="Hello":
   return 0
  elif greeting==" Hello ":
   return 0
  elif greeting=="How you doing?":
   return 20
  elif greeting=="What's happening?":
   return 100
  elif greeting=="What's up?":
   return 100
  else:
   return 100


if __name__ == "__main__":
    main()

