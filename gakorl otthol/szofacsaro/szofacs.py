import random
fonevek = ["Alma", "Korte", "taska", "Villany", "Haz", "Anna", "föld", "szék", "asztal"]
#nev = list("alma")
#random.shuffle(nev)
#print (''.join(nev))

fonev = random.choice(fonevek)
#print(fonev)

print("2. Feladat:")

if fonev[0].isupper():
    print(f"A szo tulajdonnév és {len(fonev)} karakterből áll.")
else:
    print(f"A szo koznev és {len(fonev)} karakterből áll.")
    

print("3. Feladat: ")

if fonev.lower() == fonev[::-1].lower():
    print("A szo palindrom")
else:
    print("A szo nem palidrom")    
    

print("4. Feladat: ")
print("Taladd ki a valasztott szot!")
print("""a, Megadhatom a szó maszkját, amelyben a magánhabgzók helyén csillag
      szerepel, pl: h*z*f*l*d*t""")
print("Megadhatom a szót alkotó betüket, pl: fldtáiehaza")

valasztas = input("Milyen modon segitsek? (a/b) ")
maganhangzok = ["ö","ü","ó","e","u","i","o","ő","ú","a","é","á","ű","í", "Ö","Ü","Ó","E","U","I","O","Ő","Ú","A","É","Á","Ű","Í"]

if valasztas == "a":
    for e in fonev:
        #print(e)
        if e in maganhangzok:
            print("*", end="")
        if e not in maganhangzok:
            print(e, end="")

nev = list(fonev)           
if valasztas == "b":
    random.shuffle(nev)
    print("".join(nev))
        
        
tipp = input("\nAdd meg a tippedet! ")
if tipp == fonev:
    print("Gratulalok eltalaltad!!")
else:
    print(f"Sajnalom ez nem talalt, a(z) megfelelo szo {fonev} lett volna")
    
        
