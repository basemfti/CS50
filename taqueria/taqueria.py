menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    print("Item:")
    total_cost=0

    try:

        while True:
            ch = input().title()  # Convert input to title case

            for i in menu:

             if ch==i:


                total_cost+=menu[i]


                print(f"Total:${total_cost:.2f}")
    except EOFError:

        pass


if __name__ == "__main__":
    main()
