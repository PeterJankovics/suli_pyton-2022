versenyszakaszok = ["F5.3", "NF1", "F3.2", "NF0.6", "NF0", "F2.1", "NF2"]

print("2. Feladat: ")
km = 0
for e in versenyszakaszok:
    if e[0] == "F":
        (km) += float(e[1:])
    else:
        (km) += float(e[2:])
print(f"a vesrseny távja {km} volt.")        
        
print("3. Feladat: ")
for e in versenyszakaszok[-1:]:
    if e[0] == "N":
        print("A celba gyalog ert be.")
    else:
        print("A celba futva ert be")

print("4. Feladat: ")
megall = 0
for e in versenyszakaszok:
    if e == "NF0":
        megall += 1
print(f"A verseny soran {megall} alkalommal állt meg.")

print("5. Feladat: ")
