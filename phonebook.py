peaple=[
    {"name":"basem","number": "+96213215"},
    {"name":"hakim","number": "+-98553457"},
    {"name":"fathia","number": "+-94703051"},
    ]


namee=input("gibe me name:")
for i in peaple:
   if i["name"]==namee:
      number=i["number"]
      print(f"found{number}")
      break
else:
  print("not found")





