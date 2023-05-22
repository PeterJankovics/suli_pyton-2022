class Snooker:
    def __init__(self,helyezes,nev,orszag,nyeremeny):
        self.helyezes = helyezes
        self.nev = nev
        self.orszag = orszag
        self.nyeremeny = nyeremeny

f = open("snooker.txt")
adatok = []
for szam,e in enumerate(f):
    if szam != 0:
        temp = e.strip().split(";")
        adatok.append(Snooker(*temp))

f.close()

versenyzoszam = len(adatok)
print(f"3. Feladat: A vilagranglistan {versenyzoszam} versenyzo szerepel.")
nyeremenyek = []
#nyer = sum(nyeremenyek)
for e in adatok:
    nyeremenyek.append(int(e.nyeremeny))
atlag = sum(nyeremenyek) / versenyzoszam

print(f"A versenyzok atlagosan {atlag:.2f} fontot kerestek.")

kínaiak = [ ( sor.nyeremeny, sor) for sor in adatok if sor.orszag =='Kína']
nyeremeny, adatok = max(kínaiak)
print(f'''
5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: {adatok.helyezes}
        Név: {adatok.nev}
        Ország: {adatok.orszag}
        Nyeremény összege: {adatok.nyeremeny * 380} Ft
        ''')
