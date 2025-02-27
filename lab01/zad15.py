x = input("x ")

try:
    help = eval(x)

    if isinstance(help, bool):
        print("bool")
    elif isinstance(help, float):
        print("float")
    elif isinstance(help, int):
        print("int")
    else:
        print("string")
except:
    print("string")