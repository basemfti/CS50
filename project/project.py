import pyttsx3

engine=pyttsx3.init()

def show_balance(balance):


    print("****************************")
    print(f"your balance is ${balance:.2f} ")
    engine.say(f"your balance is ${balance:.2f}")
    engine.runAndWait()

    print("****************************")


def deposit():
   print("****************************")
   amount = float (input("Enter an amount to be deposited: "))
   print("****************************")
   if amount <0:
       print("****************************")

       print("That's not a Valid amount ")
       print("****************************")
       return 0
   else: return amount



def withdraw(balance):
    print("****************************")
    amount=float(input("Enter amount to be withdrawn: "))
    print("****************************")

    if amount > balance:
        print("****************************")
        print("Insufficient funds")
        print("****************************")
        return 0
    elif amount <0:
        print("****************************")
        print("Amount must be greater than 0")
        print("****************************")
        return 0
    else:
        return amount


def main():



  balance=0
  is_runing=True


  while is_runing:


      print("****************************")
      print("      Banking Program    ")
      engine.say("Banking Program")
      engine.runAndWait()
      print("****************************")
      print("1.Show balance")
      print("2.Deposit")
      print("3.Withdraw")
      print("4.Exit")

      choice =input("Enter your choice(1-4): ")
      engine.say("Enter your choice(1-4)")
      engine.runAndWait()
      if choice =="1":
          show_balance(balance)
      elif  choice =="2":
          balance+=deposit()
      elif choice =="3":
          balance-=withdraw(balance)
      elif choice =="4":
          is_runing= False

      else :
        print("****************************")
        print("that is not Valid choice  ")
        print("****************************")


  print("****************************")
  print("Thank you have a nice day!")
  engine.say("Thank you have a nice day!")
  engine.runAndWait()
  print("****************************")



if __name__=="__main__":
    main()
