import modul0607


teglalap = [[2, 3],[5, 3],[2, 9],[1, 8],[5, 5]]
adatok = []
for e in teglalap:
    adatok.append(modul0607.teglalap(*e))

#print(adatok)

terulet = []
for e in adatok:
    temp = modul0607.teglalap.terulet(e)
    terulet.append(temp)
        
print(max(terulet))

kerulet = []
for e in adatok:
    temp = modul0607.teglalap.kerulet(e)
    kerulet.append(temp)
print(max(kerulet))
