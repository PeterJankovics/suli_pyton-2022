import random

print("1. feladat: ")
hatarertek = int(input("add meg a hatarerteket: "))
szam = random.randint(1,hatarertek)
print(szam)
tipp = int(input("Melyik szamra gomndoltam: "))
probalkozas = 1
while szam != tipp:
    probalkozas += 1
    if tipp == -1:
        print(f"a szam a {szam} lett volna")
        break
    if tipp > szam:
        print("Sajnos nem talalt.") 
        print("Kisebb szamra gondoltam.")
    else:
        print("Sajnos nem talalt.")
        print("Nagyobb szamra gondoltam")    
    tipp = int(input("Melyik szamra gomndoltam: "))

if szam == tipp:
    print(f"eltalaltad {probalkozas} probalkozasbol.")

    
