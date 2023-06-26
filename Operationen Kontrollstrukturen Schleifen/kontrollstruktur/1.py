name = input("Bitte geben sie ihren name an: ")
gender = input("Bitte geben sie ihr geschlecht an (w oder m): ")

if gender == "m":
    print(f"Guten tag Herr {name}")
elif gender == "w":
    print(f"Guten tag Frau {name}")
else:
    print("bitte gib entweder w oder m an")
    
