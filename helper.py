from boekhouding import *

def decoreer(tekst=" "):
    lengte = len(tekst) + 4
    tekst="header"
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = (bedrag) / (personen)
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):    
    uit = []
    uit.append(tekst)    
    uit.append(len(tekst) * "=")  
    return uit

# def som(inkomsten):
#     return sum(inkomsten.values())

def som(input):
    output = 0
    for key, value in input.items():
        output += value
    return output