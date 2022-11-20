nev=input("Kerek egy nevet:")
print("A " + nev + " nevet írtad be.")

print("A {belsonev} nevet írtad be.".format(belsonev=nev))

if len(nev) < 5:
    print("Ez egy jo rövid nev.")
elif len(nev) >= 10:
    print("Veri big nev")

be="nemvégjel"
szavak=[]
while be !="":
    be=input("írj be valamit:")
    szavak.append(be)
# szavak.remove("")
# szavak.pop(len(szavak)-1)
szavak=szavak[:1]
print(szavak)    
