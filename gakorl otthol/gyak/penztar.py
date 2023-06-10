f=open("penztar.txt")
termekek = []
for sor in f:
    temp = sor.replace("\n", "")
    termekek.append(temp)

f.close()
print(termekek)


print("A fizetesek szama: {}".format(termekek.count("F")))
termekekszama = 0
elsof = termekek.index("F")
for e in range(len(termekek)):
    if e < elsof:
        termekekszama += 1

print("AZ elso versenyzo {} darab arucikket vasarolt".format(termekekszama))        
str(termekek)
print()
