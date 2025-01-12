def main():

    print("camelCase:")
    ch=input("")

    x=camel(ch)
    print("snake_Case:",x)


def camel(bes):
    snake=""
    for i in bes :
        if i.isupper():
          snake+="_"+i.lower()
        else:
          snake+=i

    return snake

main()




