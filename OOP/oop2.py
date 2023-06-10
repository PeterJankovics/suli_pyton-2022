class kor:
    def __init__(self, sugar, kozeppontx, kozepponty):
        self.sugar = sugar
        self.kozeppontx = kozeppontx
        self.kozepponty = kozepponty
    def terulet(self):
        return self.sugar * (3.14 ** 2)
    def kerulet(self):
        return 2 * 3.14 * self.sugar

class okoskor(kor):
    def __init__(self, sugar, kozeppontx, kozepponty, szin):
        super().__init__(sugar, kozeppontx, kozepponty,)
        self.szin = szin
    def nagyitas(self, szazalek):
        self.sugar *= (1 + szazalek / 100)

kor1 = kor(4, 5, 6,)
okoskor1 = okoskor(4, 5, 6, "kek")       

okoskor1.nagyitas(50)
#print(okoskor1.sugar)



class ember:
    def __init__(self, szuletes, magassag, testsuly):
        self.szuletes = szuletes
        self.magassag = magassag
        self.testsuly = testsuly
    def eletkor(self):
        return 2023 - self.szuletes
    def TTI(self):
        return self.testsuly / (self.magassag / 100) ** 2

class diak(ember):
    def __init__(self, szuletes, magassag, testsuly, evfolyam):
        super().__init__(szuletes, magassag, testsuly)
        self.evfolyam = evfolyam
    def osztaly(self):
        eletkor = self.eletkor()
        if 6 <= eletkor < 19:
            return eletkor - 5
        else:
            return "felnottoktatas"


ember1 = ember(2008, 163, 65)
print(ember1.eletkor())
print(ember1.TTI())

diak1 = diak(2017, 163, 65, "A")
print(diak1.osztaly())


