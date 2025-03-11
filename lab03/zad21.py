import random

def kamien_papier_nozyce():
    opcje = ["kamień", "papier", "nożyce"]
    
    while True:
        wybor_uzytkownika = input("wybierz: ").lower()
        
        if wybor_uzytkownika == "koniec":
            break
        
        if wybor_uzytkownika not in opcje:
            print("Niepoprawny wybór")
            continue
        
        wybor_komputera = random.choice(opcje)
        print(wybor_komputera)
        
        if wybor_uzytkownika == wybor_komputera:
            print("Remis!")
        elif (wybor_uzytkownika == "kamień" and wybor_komputera == "nożyce") or \
             (wybor_uzytkownika == "papier" and wybor_komputera == "kamień") or \
             (wybor_uzytkownika == "nożyce" and wybor_komputera == "papier"):
            print("Wygrałeś!")
        else:
            print("Przegrałeś!")
        
        print("---")

kamien_papier_nozyce()
