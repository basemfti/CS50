
def main():
    grocery_items = {}

    try:
        while True:
            item = input().strip().lower()
            if item in grocery_items:
                grocery_items[item] += 1

            else:
                grocery_items[item] = 1
    except EOFError:
        pass


    for item, count in sorted(grocery_items.items()):
        print(f"{count} {item.upper()}")

main()
