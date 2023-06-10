furdo = []

f = open("furdoadat.txt")
for egysor in f:
    temp = egysor.replace("\n", "").split(" ")
f.close()

