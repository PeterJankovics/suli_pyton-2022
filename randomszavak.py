
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
    print(e[0].ljust(10), str(e[1]).rjust(4) , "kg")
