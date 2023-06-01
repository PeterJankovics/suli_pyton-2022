szoveg = str(input("kerek egy szoveget: "))
szam = ""
while type(szam) != int:   
    try:
        szam = int(input("Kerek egy szamot: "))
    except:
        print("Ez nem egy egesz szam!")
print(szoveg[szam]*szam)
