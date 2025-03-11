import math

def czy_wspolliniowe(P1, P2, P3):
    return (P2[0] - P1[0]) * (P3[1] - P1[1]) == (P3[0] - P1[0]) * (P2[1] - P1[1])

def odleglosc(P1, P2):
    return math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)

def obwodTrojkata(P1, P2, P3):
    if czy_wspolliniowe(P1, P2, P3):
        print("Punkty są współliniowe - nie tworzą trójkąta.")
        return 0
    return odleglosc(P1, P2) + odleglosc(P1, P3) + odleglosc(P2, P3)

P1 = [0, 0]
P2 = [0, 4]
P3 = [4, 4]

print(obwodTrojkata(P1, P2, P3))