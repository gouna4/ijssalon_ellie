from helper import decoreer
## Les7
def print_aanbieding():
    prijzen = {
        "aardbei": 3,
        "vanille": 4,
        "chocolade": 5
    }
    # # op aangeven van Peter vanille vervangen door aardbei.
    aanbieding = prijzen["aardbei"] * 0.8
    # # # Om te testen aanbieding
    #print(aanbieding)

    reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}"
    # # # Om te testen reclame_tekst
    #print(reclame_tekst)

    reclame_tekst2 = reclame_tekst[:62]
    # # Om te testen reclame_tekst2
    #print(reclame_tekst2)

    reclame_tekst3 = reclame_tekst2.upper()
    # # Om te testen reclame_tekst3
    #print(reclame_tekst3)

    reclame_tekst4 = reclame_tekst3.split()
    # # Om te testen reclame_tekst4
    #print(reclame_tekst4)

    # #Om te testen reclame_tekst4 met for loop
    # for el in reclame_tekst4:
    #    print(el)

    # #Om te testen reclame_tekst4 met for loop en lower
    # for el in reclame_tekst4:
    #     print(el.lower())

    # # eind resultaat.. Hoop dat het goed is :)
    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el.upper())
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()
