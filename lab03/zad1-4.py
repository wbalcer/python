def pietro(z):
    print(4 * z + "[]" + 3 * z)

def dach(z):
    h = (10 // 2) + 1   
    for i in range(1, 10 + 1, 2):
        s = (10 - i) // 2
        print(" " * s + z * i + " " * s)

def rysuj_dom(p, zp, zd):
    dach(zd)
    for i in range(p):
        pietro(zp)

rysuj_dom(4, "$", "@")