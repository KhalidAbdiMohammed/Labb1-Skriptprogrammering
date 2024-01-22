import random

def gissningspelet():

    svar = random.randint(1,60)
    print("Gissa på heltal mellan 1-60")
    while True:
        gissaTal = int(input())
        if gissaTal == svar:
            print("Du gissade rätt! Bra jobbat!")
            break
        elif gissaTal > svar:
            print ("För högt gissat, prova igen!")
        elif gissaTal < svar:
            print("För lågt gissat, prova igen!")


def egental(valfritt1, valfritt2):
    tal_lista = []

    for tal in range(1,1601):
        if tal % valfritt1 == 0 and tal % valfritt2 == 0:
            tal_lista.append(tal)

    return tal_lista