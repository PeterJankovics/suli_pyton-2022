import modul, random

f = open("szavak.txt")        

lista = (f.read().strip().replace("\"","").split(", "))
    
f.close()        

szavak = []
for e in lista:
    szavak.append(modul.szo(e))

#print(szavak)    

rejtett = random.choice(szavak)
#print(rejtett.szo)
tippek = []
while True:
    be = input("Kerem a tippet: ")
    tippek.append(be)
    if be == "stop":
        break
    vissza = rejtett.minta(be)
    print(f"Az eredmeny: {vissza}")    
    if vissza == be:
        break
if tippek[-1] == "stop":
    pass
else:
    print(f"len{tippek}tippelesstl talalta ki")
