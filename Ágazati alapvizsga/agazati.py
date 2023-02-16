print("1. feladat")

szoveg = input("Kerek egy szöveget: ")
szam = ""
while type(szam) != int: 
    try:
        szam = int(input("Kerek egy egesz szamot: "))
    except:
        print("EZ nem egesz szam")
try:    
    print(szoveg[szam -1]*szam)
except:
    print("Nincs ilyen betű!")
