"""Ország:	Állatok (Animalia)
Törzs:	Gerinchúrosok (Chordata)
Altörzs:	Gerincesek (Vertebrata)
Főosztály:	Négylábúak (Tetrapoda)
Osztály:	Emlősök (Mammalia)
Alosztály:	Elevenszülő emlősök (Theria)
Csoport:	Eutheria
Alosztályág:	Méhlepényesek (Placentalia)
Öregrend:	Laurasiatheria
Csoport:	Ferae
Rend:	Ragadozók (Carnivora)
Alrend:	Kutyaalkatúak (Caniformia)
Család:	Kutyafélék (Canidae)
Alcsalád:	Valódi kutyaformák (Caninae)
Nemzetség:	Rókák (Vulpini)
Nem:	Róka (Vulpes)
Frisch, 1775"""


class orszag():
    def __init__(self, o):
        self.orszag = o
class torzs(orszag):
    def __init__(self, o, t):
        super().__init__(o)
        self.torzs = t
class altorzs(torzs):
    def __init_(self, o,t,at):
        super.__init__(o,t)
        self.altorzs = at
class foosztaly(altorzs):
    def __init__(self, o, t, at, fo):
        super().__init__(o, t, at)
        self.foosztaly = fo
class osztaly(foosztaly):
    def __init__(self,o, t, at, fo, osz):
        super().__init__(o, t, at, fo)
        self.osztaly = osz
class alosztaly(osztaly):
    def __init__(self,o, t, at, fo, osz, al):
        super().__init__(o, t, at, fo, osz)
        self.altorzs = al
class csoport(alosztaly):
    def __init__(self,o, t, at, fo, osz, al, cso):
        super().__init__(o, t, at, fo, osz, al)
        self.csoport = cso        
class alosztalysag(csoport):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz):
        super().__init__(o, t, at, fo, osz, al, cso)
        self.alosztaly = alosz  
class oregrend(alosztalysag):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz, oreg):
        super().__init__(o, t, at, fo, osz, al, cso, alosz)
        self.oregrend = oreg
class csoport2(oregrend):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz, oreg, csop2):
        super().__init__(o, t, at, fo, osz, al, cso, alosz, oreg)
        self.csoport2 = csop2
class rend(csoport2):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r):
        super().__init__(o, t, at, fo, osz, al, cso, alosz, oreg, csop2)
        self.rend = r
class alrend(rend):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, alr):
        super().__init__(o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r)
        self.alrend = al
class csalad(alrend):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, alr, csal):
        super().__init__(o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, al)
        self.csalad = csal        
class alcsalad(csalad):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, alr, csal, alcsal):
        super().__init__(o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, al, csal)
        self.alcsalad = alcsal
class nemzetseg(alcsalad):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, alr, csal, alcsal, nemz):
        super().__init__(o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, al, csal, alcsal)
        self.nemzetseg = nemz 
class nem(nemzetseg):
    def __init__(self,o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, alr, csal, alcsal, nemz, nem):
        super().__init__(o, t, at, fo, osz, al, cso, alosz, oreg, csop2, r, al, csal, alcsal)
        self.nem = nem         




        
