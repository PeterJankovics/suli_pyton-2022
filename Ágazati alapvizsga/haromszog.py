def haromszog():
    vissza = []
    for i in range(3):
        szam = ""
        while szam == "":
            try:
                szam = int(input("Kerek egy szamot: "))
            except:
                print("Ez nem egy szam!")
        vissza.append(szam)
    return vissza
            


