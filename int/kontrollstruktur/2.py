note = input("note in punkten: ")

noten = {
    0: "6",
    1: "5-",
    2: "5",
    3: "5+",
    4: "4-",
    5: "4",
    6: "4+",
    7: "3-",
    8: "3",
    9: "3+",
    10: "2-",
    11: "2",
    12: "2+",
    13: "1-",
    14: "1",
    15: "1+"
}
try:
    print(f"Deine Note ist {noten[int(note)]}")
except:
    print("####")