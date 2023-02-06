f = open("valaszok.txt","r")

adatok = f.read().split("\n")
adatok.remove("")
f.close()
# print(adatok)

helyes = adatok[0]

adatok.remove(helyes)
valaszok = []

for e in adatok:
    valaszok.append(e.split(" "))

























