def istSchaltjahr(jahr):
    if jahr % 4 == 0:
        if jahr % 100 == 0:
            if jahr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def istGültigeDatum(tag, monat, jahr):
    monate_mit_31_tagen = [1, 3, 5, 7, 8, 10, 12]
    monate_mit_30_tagen = [4, 6, 9, 11]

    if monat < 1 or monat > 12:
        return False

    if monat in monate_mit_31_tagen:
        if tag < 1 or tag > 31:
            return False
    elif monat in monate_mit_30_tagen:
        if tag < 1 or tag > 30:
            return False
    else:  # Februar
        if istSchaltjahr(jahr):
            if tag < 1 or tag > 29:
                return False
        else:
            if tag < 1 or tag > 28:
                return False

    return True


datum = input("Bitte geben Sie ein Datum im Format TT.MM.JJJJ ein: ")

datum_split = datum.split('.')
tag = int(datum_split[0])
monat = int(datum_split[1])
jahr = int(datum_split[2])

if istGültigeDatum(tag, monat, jahr):
    print("Das eingegebene Datum ist gültig.")
else:
    print("Das eingegebene Datum ist ungültig.")
