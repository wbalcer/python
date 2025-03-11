def szukajWLiscie(lista, a):
    if isinstance(a, (int, float)):
        wartosc = a
    elif isinstance(a, str):
        if a.isdigit():
            wartosc = int(a)
        elif a.replace('.', '', 1).isdigit():
            wartosc = float(a)
        else:
            wartosc = sum(ord(c) for c in a)
    elif isinstance(a, bool):
        wartosc = int(a)
    else:
        raise TypeError("Nieobsługiwany typ argumentu a")
    
    liczba_wystapien = lista.count(wartosc)
    print(f'Liczba wystąpień {wartosc} w liście: {liczba_wystapien}')
    return liczba_wystapien

# Przykład użycia
lista_liczb = [1, 2, 3, 4, 2, 2, 5, 6, 2, "42", "abc", 97, True, False]
a = "42"
szukajWLiscie(lista_liczb, a)