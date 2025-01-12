import inflect
def bid_adieu(names):
    p = inflect.engine()
    num_names = len(names)

    if num_names == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif num_names == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}"
        farewell += f", {'and ' + names[-1]}"
        
        return farewell


def main():
    names = []
    try:
        while True:
            name = input("Name:")
            names.append(name)
    except EOFError:
        pass

    print(bid_adieu(names))

if __name__ == "__main__":
    main()



