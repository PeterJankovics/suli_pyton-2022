
import random
szavak = ["alma","körte","banán","dinnye","barac",]
# szandom szó kiirasa
# random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))

print("-"*52)

nagylista = []
for e in szavak:
    print(e)
    kislista = []
    kislista.append(e)
    kislista.append(random.randint(12,312))
    print(kislista)
    nagylista.append(kislista)
    
print(nagylista)    

for e in nagylista:
    print(e[0].ljust(10), str(e[1]).rjust(4) , "kg", "-"*(e[1]//10))


print("-"*134)


minert = int(input("Add meg hogy hol kezdődjön!!! "))
maxert = int(input("Add meg a maxot!!! "))
darab = int(input("hanayat kérsz??? "))

l = []

for i in range(darab):
    l.append(random.randint(minert, maxert))
print(l)

legnagyobb = max(l)
egyseg = 80//legnagyobb
for e in l:
    print("*"*(e*egyseg))










    
