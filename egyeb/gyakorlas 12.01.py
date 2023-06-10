def oszlopba(munkalista,db):
    for i in range(len(szam)):
        print(szam[i],end = " ")
        if i % db == db-1:
            print()
    print()        
    
szam = [324, 1234, 2134, 342, 234, 34, 3, 2, 54, 23]
for i in range(0):
    szam.append(int(input("kerek egy szamot: ")))
print(szam)

for i in range(len(szam)):
    print(szam[i],end = " ")
    if i % 3 == 2:
        print()
print()        
szambe = int(input("Kérek egy számot: "))
if szambe in szam:
    print("MAR VOLT!!4!44!!")
else:
    print("nincs benne")

oszlopba(szam, 5)
