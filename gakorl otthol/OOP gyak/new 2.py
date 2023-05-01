class myclass:
    x = 5
    def megnovel(self, mennyivel = 1):
        self.x += mennyivel


class kutya:
    nev, fajta, agresszivitas, kor, szin = ["","",0,0,""]
    def __init__(self, nev, fajta, agresszivitas, kor, szin):
        self.nev = nev
        self.fajta = fajta
        self.agresszivitas = agresszivitas
        self.kor = kor
        self.szin = szin
    def ugat(self):
        print("VAU VAU")
    def koszon(self):
        print(f"VAU VAU a nevem {self.nev}")
    def talalkozas(self, masik):
        print(f"szasz a nevem {self.nev}.")
        print(f"szeva az enyem meg {masik.nev}.")
        if self.kor > 5:
            print("latom oreg vagy")
        else:
            print("milyen fiatal itt valaki.")
        if masik.kor > 5:
            print("te pedig milyen fiatal vagy.")
        else:
            print("hat azert mar te is benne vagy a korban.")
    def kerdes (self, masik)    
k1 = kutya("Bodri", "puli", 3, 5, "fekete")
k2 = kutya("Vaur", "haski", 5, 6, "szurke")


k1.talalkozas(k2)

