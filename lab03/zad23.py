class Person:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} i mam {self.wiek} lat.")

osoba = Person("Jan", 30)
osoba.przedstaw_sie()