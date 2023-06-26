startwert = float(input("Startkapital: "))
zinssatzt = float(input("Zinssatzt in %: "))
jahre = int(input("Wie viele jahre: "))
zinssatzt = zinssatzt / 100 + 1

for num in range(jahre):
    startwert = startwert * zinssatzt
    print(f"Nach {num + 1} jahren hast du {startwert} euro")
