def adatbekeres():
    print("I/A:")
    muzeum_neve = input("\tMúzeum neve: ")
    latogato_neve = input("\tLátogató neve: ")
    ertekeles = int(input("\tÉrtékelés (1-20): "))

    if ertekeles <= 0:
        kimeno = "Az értékelés nem lehet negatív vagy 0!"
    elif ertekeles > 20:
        kimeno = "20 pont feletti értékelés nem elfogadható!"
    else:
        kimeno = "Köszönjük az értékelést!"

    print(f"I/B:\n\t{kimeno}")