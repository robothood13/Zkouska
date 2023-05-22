from pojisteny import Pojisteny
from seznam_pojistovny import SeznamPojisteny


seznam_pojisteny = SeznamPojisteny()

while True:
    print("1 - Vytvořit pojištěného")
    print("2 - Zobrazit seznam pojištěných")
    print("3 - Vyhledat pojištěného")
    print("0 - Ukončit program")

    volba = input("Vyberte akci: ")

    if volba == "1":
        jmeno = input("Zadejte jméno:\n")
        prijmeni = input("Zadejte příjmení:\n")
        vek = int(input("Zadejte věk:\n"))
        telefon = input("Zadejte telefonní číslo:\n")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        seznam_pojisteny.pridej_pojisteneho(pojisteny)
        print("Pojištěný byl úspěšně přidán do seznamu.")

    elif volba == "2":
        seznam_pojisteny.zobraz_seznam()

    elif volba == "3":
        jmeno = input("Zadejte jméno:\n")
        prijmeni = input("Zadejte příjmení:\n ")
        pojisteny = seznam_pojisteny.vyhledej_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            print(pojisteny.jmeno, pojisteny.prijmeni, pojisteny.vek, pojisteny.telefon)
        else:
            print("Pojištěný nebyl nalezen.")

    elif volba == "0":
        break

    else:
        print("Neplatná volba.")

# Snad to funguje...
