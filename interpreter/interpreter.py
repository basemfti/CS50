
print("Expression")
ch=input("")
x=float(ch.split( )[0])

op=ch.split( )[1]

z=float(ch.split( )[2])

#x=float(input(""))
#op=input("")
#z=float(input(""))

if op == '+':
 print (x + z)
elif op == '-':
    print (x - z)
elif op == '*':
    print(x * z)
elif op == '/':
    print (x / z)
else:
 print ("None")


