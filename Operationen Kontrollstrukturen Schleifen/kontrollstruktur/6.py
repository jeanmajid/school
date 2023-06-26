monat = input("Bitte geben Sie den Monat (als Zahl) ein: ")

monat = int(monat)

if monat == 2:
    jahr = input("Bitte geben Sie das Jahr ein: ")
    jahr = int(jahr)

    if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
        anzahl_tage = 29
    else:
        anzahl_tage = 28
elif monat in [4, 6, 9, 11]:
    anzahl_tage = 30
else:
    anzahl_tage = 31

print("Der Monat", monat, "hat", anzahl_tage, "Tage.")
