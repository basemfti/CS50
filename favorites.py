from cs50 import SQL

db=SQL("sqlite:///favorites.csv")

favorite=input("favorite: ")

rows=db.execute("SELECT COUNT(*) as n From favorites WHERE problem=?",favorite)
row=rows[0]

print(row[n])
