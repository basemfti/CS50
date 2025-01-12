my_dict ={"apple": 130,"avocado": 50,"sweet cherries": 100,"kiwifruit":90,"pear":100}

ch=input("Items:" )
for i in my_dict:
    if ch.lower()==i :
        print("Calories",my_dict[i])
