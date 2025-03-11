def cesar(tekst, klucz):
    zaszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():
            przesuniecie = klucz % 26
            if znak.islower():
                nowy_znak = chr((ord(znak) - ord('a') + przesuniecie) % 26 + ord('a'))
            else:
                nowy_znak = chr((ord(znak) - ord('A') + przesuniecie) % 26 + ord('A'))
            zaszyfrowany_tekst += nowy_znak
        else:
            zaszyfrowany_tekst += znak
    return zaszyfrowany_tekst

tekst = "Hello world"
klucz = 3
zaszyfrowany = cesar(tekst, klucz)
print(zaszyfrowany)
