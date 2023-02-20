def id
# 1. feladat

eredmenyek = []

f = open("triatlon.txt",)

for egysor in f:
    temp = egysor.replace("\n","").split(";")
    eredmenyek.append(temp)
    
f.close()
eredmenyek.pop(0)

# 2. feladat
print("2. feladat:")
print("A versenyen {} versenyzo indult.".format(len(eredmenyek)))

# 3. feladat
print("3. feladat:")
