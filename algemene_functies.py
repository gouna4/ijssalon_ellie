# Ik heb het aanroepen van het programa in de main geplaatst.
#als dat niet de boedoeling is. kan het in comentaar gezet worden en wat nu in comentaar staat er uit er uit halen.
def mijn_functie_1(Nummer):
    Tabel = {2:4 ,
             4:16,
            10:100,
            12:144 }
    if Nummer in Tabel:
        return Tabel[Nummer]
    else:
        print('mijn_functie_1: Nummer komt niet voor in tabel ')


#print("Resultaat mijnn_functie_1 ", mijn_functie_1(10))


def mijn_functie_2(Nummer):
    Tabel = {((12,3)):[15, 9, 36, 4] ,
             ((12,2)):[14, 10, 24, 6],
            ((10,5)):[15, 5, 50, 2],
            ((100,20)):[120, 80, 2000, 5] }
    if Nummer in Tabel:
        return Tabel[Nummer]
    else:
        print('mijn_functie_2: Nummer komt niet voor in tabel')

#print(mijn_functie_2((10,5)))

def mijn_functie():
    print(mijn_functie_1(10))
    print(mijn_functie_2((10,5)))



if __name__ == "__main__":
 mijn_functie()
    