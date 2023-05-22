f = open("valaszok.txt")
adatok = f.read().split("\n")[:-1]
f.close()

print(adatok)
