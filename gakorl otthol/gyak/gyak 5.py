print("1. feladat: ")
fordulok = int(input("fordulok szama: "))


print("2. feladat: ")
golkul = []
for e in range( fordulok ):
    fordulo = int(input("forduoban a kulombseg: "))
    golkul.append(fordulo)
print(golkul)


print("3. feladat: ")
gyozelem = 0
veszteség = 0
dontetlen = 0
for golkulo in golkul:
    if golkulo > 0:
        gyozelem = gyozelem +1
    elif golkulo == 0:
        dontetlen = dontetlen + 1
    else:
        veszteség = veszteség + 1
print("a szezonban a csapatnak ", gyozelem, "gyozelme", veszteség, "vesztesége", dontetlen," dontetlene volt." )

print("4. feladat: ")
print(f"A csapatnak osszesen {gyozelem * 3 + dontetlen} pontja lett.")

print("5. feladat: ")
if gyozelem > veszteség + dontetlen:
    print("a csapatnak tobb gyozelme volt mint veresége. ")
else:
    print("a csapatnak tobb veresege volt mint gyozelme")


print("6. feladat: ")
sikeres = 0
for index in range(fordulok -1):
    if 0 < golkul[index] < golkul[index +1]:
        sikeres += 1
if sikeres != 0:
    print("a")
else:
    print("b")
    
