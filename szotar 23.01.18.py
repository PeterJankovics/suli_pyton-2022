# Készítsetek egy programot,
# ami a szavak tanulásában segíthet.
# Legyen egy függvény, ami bekér egy szót és annak jelentését.
# Ezek kerüljenek egy fileba, hozzáfűzéssel.
# A második felében készítsetek egy olyan függvényt,
# ami betölti a file-t, majd sorsol 1 szót,
# hozzá 3 rossz választ és rákérdez, melyik lehet a jó.
# Fusson le többször, pontozzon, osztályozzon.


import random

def szobeker():
    szo = input("Kerek egy szot! ")
    if szo == "":
        jelentes == ""
    else:
        jelentes = input(szo + " jelentes")

    return [szo, jelentes]

szavak = []

def sokbeker():
    szo = szobeker()
    while szo [0] != "":
        szavak.append(szo)
        szo = szobeker()
    
    return szavak

def filebair(lista):
    f=open("szotar.txt","a")
    f.close
    

