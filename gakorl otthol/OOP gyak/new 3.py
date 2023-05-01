import random
class kor:
    def __init__(self, sugar, kozeppont=0):
        self.sugar = sugar
        self.kozeppont = kozeppont
    def terulet(self):
        return self.sugar * pow(3.14, 2)
    def kerulet(self):
        return self.sugar * 3.14 *2

#korok = []
#for e in range(5):
#    kor1 = kor(random.randint(1, 10))
#    korok.append(kor1)
    
#for kor in korok:
#    print(kor.sugar, kor.kerulet())

class okoskor(kor):
    def __init__(self, sugar, kozeppont, szin):
        super().__init__(sugar, kozeppont)
        self.szin = szin


kor1 = okoskor(3,4,"sarga")



class ember:
    def __init__(self, szuletes, magassag, testsuly):
        self.szuletes = szuletes
        self.magassag = magassag
        self.testsuly = testsuly
    def eletkor(self):
        return 2023 - self.szuletes
    def TTI(self):
        return self.testsuly / (self.magassag ** 2)
class diak(ember):
    def __init__(self, szuletes, magassag, testsuly, betujel):
        super().__init__(szuletes, magassag, testsuly)
        self.betujel = betujel
    def evfolyam(self):
        eletkor = self.eletkor()
        if 6 <= eletkor < 19:
            return eletkor - 5
        else:
            return "felnottoktatas"
            
ember1 = ember(2007, 178, 75)
ember2 = ember(2004, 122, 40)
ember3 = ember(2000, 155, 80)
print(ember1.eletkor())
print(ember1.TTI())
print(ember2.eletkor())
print(ember2.TTI())
print(ember3.eletkor())
print(ember3.TTI())

diak1 = diak(2007, 178, 75, "A")
diak2 = diak(2004, 122, 40, "B")
diak3 = diak(2000, 155, 80, "C")

print(diak1.evfolyam())
print(diak2.evfolyam())
print(diak3.evfolyam())
