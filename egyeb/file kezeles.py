f = open("proba.txt","w")
f.write("helloka")
f.write("\n")
f.write("vilag")       
f.close()

f = open("proba.txt","r")
szoveg = f.read()
sorok = szoveg.split("\n")
print(sorok)
f.close()

f = open("proba.txt","r")
sorok = []
for sor in f:
    sorok.append(sor.replace("\n","").replace("\r",""))
print(sorok)    
f.close()

