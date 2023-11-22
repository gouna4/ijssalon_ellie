from algemene_functies import mijn_functie_2



def aanbieding_1(smaak, prijs ,korting):
    prijs_korting = prijs*korting
    te_betalen = prijs - prijs_korting
    return f'Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} euro voor {te_betalen} euro.'

print(aanbieding_1('aardbei',4,0.1))


def inkomsten_totaal(inkomsten,btw):
     
        return f"Het totaal van alle inkomsten van deze week is {Week} euro, waarover {Btw_betalen } euro btw betaald dient te worden"

inkomsten_per_dag_van_deze_week = [220,430,125,160,205,90,345]
btw= 0.09
Week= sum (inkomsten_per_dag_van_deze_week)
Btw_betalen= btw * sum(inkomsten_per_dag_van_deze_week)

print(inkomsten_totaal(inkomsten_per_dag_van_deze_week,Btw_betalen))



def laag_en_hoog(mijn_lijst):

    return max(lijst) ,min (lijst)
lijst = [220,430,125,160,205,90,345]   

print(laag_en_hoog(lijst))


def gemiddelde(mijn_lijst):
    gemiddelde_waarde_lijst = sum(inkomsten_per_dag_van_deze_week) / len(inkomsten_per_dag_van_deze_week)
    
    return gemiddelde_waarde_lijst

inkomsten_per_dag_van_deze_week = [220, 430, 125, 160, 205, 90, 345]

mijn_lijst = gemiddelde(inkomsten_per_dag_van_deze_week)

print("De gemiddelde inkomste deze week zijn",gemiddelde(mijn_lijst),"euro")



def meervoudig(invoer_lijst):
    return max(invoer_lijst) ,min (invoer_lijst)


lijst = [10,5,3,2,1,2,9] 
print("De laagste en hoogste zijn: ", laag_en_hoog(lijst))
    

def combinatie(invoer_lijst_2):
    
    korte_lijst = meervoudig(invoer_lijst_2) # return value max,min
    resultaat = mijn_functie_2(korte_lijst)  # return value list

    return resultaat

lijst = [10,5]
print(combinatie(lijst))

# Importeer op de eerste regel van het bestand ‘aanbieding.py’ de functie mijn_functie_2 uit het bestand ‘algemene_functies.py’.

# Plaats in het bestand ‘reclame.py’ een functie genaamd combinatie(), die één parameter bevat, genaamd invoer_lijst_2. In deze functie roept u de functie meervoudig() aan, met als argument de parameter invoer_lijst_2.

# De teruggeefwaarde van deze functie dient te worden opgeslagen in variabele korte_lijst. Deze korte lijst dient als argument gebruikt te worden bij het aanroepen van functie mijn_functie_2. De teruggeefwaarde 
# die hierdoor gegenereerd wordt, is de teruggeefwaarde van functie combinatie().