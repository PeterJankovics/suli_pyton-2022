import random

def szobeker ():
    szo = input("kerek szot! ")
    if szo == "":
        jelentes = ""
    else:
        jelentes = input(szo + "jelentese: ")
    return [szo, jelentes]


szavak = []
def sokbeker ():
    szo = szobeker()
    while szo[0] != "":
        szavak.append(szo)
        szo = szobeker()



    return szavak


def filebair(lista):
    f = open("szotar.txt", "a")
    
    f.close()
