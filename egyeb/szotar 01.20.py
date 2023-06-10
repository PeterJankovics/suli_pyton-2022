#AEz a függvény bekér egy szót, és annak jelentését.
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

    rossz = []
    for i in range(3):
        temp = random.choice(kerdesek)
        
        while not(temp not in rossz and temp != valasztott): 
            temp = random.choice(kerdesek)    
        rossz.append(temp)
        #print("rossz",rossz)    
    print("-"*100)
    print("Mit jelent: " + valasztott[0] + "?")

    rossz.append(valasztott)
    #valasz bekeres
    abc = "abcdefghijklmnopqrstuvwxyz"
random.shuffle(rossz)
    i = 0
    for e in rossz:
        print(abc[i]", "+e[1])
        i += 1
    valasz = input("valassz: ")
    hol = 4
    while hol >= 4:
        try:
            if valasz != "":
                hol = abc.index(valasz)               
        except:
            valasz = input("valassz ujra!! ")
        else:
            if hol >= 4:
                valasz = input("valassz ujra!! ")

    #if valasztott[0] == rossz[hol][0]:
    #    print("Helyes :)")
    #else:
    #    print("Rossz valasz")
    return valasztott[0] == rossz[hol][0]

def menu():
    beker = ""
    while beker != "0":
        print("-"*40)
        print("Szotar program\n")
        print("1: Szavak bevitele")
        print("2: Feleltetes")
        print("0: Kilepes")
        beker = input("valasz: ")
    
        if beker == "1":
            szavak = sokbeker()
            filebair(szavak)
        elif beker == "2":
            #feleltetés                
            beolvas()
            lil_A = []
            for i in range(10):
                lil_A.append(kerdez())
    
            #print(lil_A)

            print("Az eredmény:{:.0%}".format(lil_A.count(True)/len(lil_A)))

                
            
menu()



#szavak=sokBeker()
#filebaIr(szavak)
