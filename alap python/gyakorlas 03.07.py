gyumolcsok = ["alma", "korte", "banan", "eper", "malna", "szolo", "barac"]
print("ennyi gyumolcs van " + str(len(gyumolcsok)))


print(gyumolcsok[6])
#gyumolcsok[6] += "k"
print(gyumolcsok.index("barac"))
#gyumolcsok[gyumolcsok.index("barac")] += "k"
index = gyumolcsok.index("barac")
gyumolcsok[index] + "k"
print(gyumolcsok[6])

print("rovid gyumolcsok")
#for i in range(len(gyumolcsok)):
#    if len(gyumolcsok[i]) < 5:
#        print(gyumolcsok[i])

    
rovid = []    
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i]) < 5:
        rovid.append(gyumolcsok[i])
print(rovid)


rovida = []
for e in gyumolcsok:
    if len(e) < 5:
        rovida.append(e)       
print(rovida)


rovidb = [e for e in gyumolcsok if len(e) < 5]
print(rovidb)

rovidc = [] 
i = 0
while i < len(gyumolcsok):
    if len(gyumolcsok[i]) < 5:
        rovidc.append(gyumolcsok[i])
    i += 1
print(rovidc)

rovidd = []
i = 0
while True:
    print(i)
    if len(gyumolcsok[i]) < 5:
        rovidd.append(gyumolcsok[i])
    if len(gyumolcsok) -1 == i:
        break
    i += 1

print(gyumolcsok[:2])
print(gyumolcsok[-2:])
print(gyumolcsok[len(gyumolcsok)-2:])


print(gyumolcsok[1:-1])


paratlan = gyumolcsok[1::2]
print(paratlan)

paros = gyumolcsok[0::2]
print(paros)
masolat = gyumolcsok
print(masolat)
masolat.reverse()
print(masolat)
print(", ".join(masolat[]))

