print("Programm zur Lösung linearer Gleichungen (ax + b = 0)")
print("----------------------------------------------------")

# Benutzereingabe für a und b
a = float(input("Bitte den Wert für a eingeben: "))
b = float(input("Bitte den Wert für b eingeben: "))

# Berechnung der Lösung
if a == 0:
    if b == 0:
        print("Jede Zahl ist eine Lösung.")
    else:
        print("Die Gleichung hat keine Lösung.")
else:
    x = -b / a
    print("Die Lösung lautet:", x)
