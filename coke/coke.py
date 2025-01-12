def main():
    # Constants
    COKE_PRICE = 50
    ACCEPTED_COINS = [25, 10, 5]

    # Variables
    amount_inserted = 0

    # Prompt user to insert coins until at least 50 cents are inserted
    while amount_inserted < COKE_PRICE:
        print(f"Amount Due: {COKE_PRICE - amount_inserted}")
        coin = int(input("Insert coin"))
        if coin in ACCEPTED_COINS:
            amount_inserted += coin

    # Calculate change
    change = amount_inserted - COKE_PRICE

    # Output change

    if change >0:
           print(f"Change Owed: {change}")
    else:
           print(f"Change Owed: {change}")



if __name__ == "__main__":
    main()









