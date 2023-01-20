#Ez a függvény bekér egy szót, és annak jelentését.
#Visszaad: a két bekérés listában
import random
def szoBeker():
    szo=input("Kérek egy szót: ")
    if szo=="":
        jelentes=""
    else:
        jelentes=input(szo+ " jelentése: ")
    return [szo,jelentes]

szavak=[]
def sokBeker():
    szo=szoBeker()
    while szo[0]!="":
        szavak.append(szo)
        szo=szoBeker()
       
    return szavak


def filebaIr(lista):
    f=open("szotar.txt","a")

    for e in lista:
        #print(e)
        f.write(" ".join(e))
        f.write("\n")

       
    f.close()

kerdesek=[]
def beolvas():
    f=open("szotar.txt","r")
    for sor in f:
        #apple alma
        kerdesek.append(sor.replace("\n","").split(" "))
    f.close()


def kerdez():
    valasztott = random.choice(kerdesek)    
    print(valasztott)
    rossz = []
    for i in range(3):
        temp = random.choice(kerdesek)
        print(temp)
        while temp not in rossz and temp != valasztott :
            rossz.append(temp)
        print(rossz)    
    print("-"*100)
    print("Mit jelent: " + valasztott[0] + "?")

    rossz.append(valasztott)
        

beolvas()
kerdez()

#szavak=sokBeker()
#filebaIr(szavak)