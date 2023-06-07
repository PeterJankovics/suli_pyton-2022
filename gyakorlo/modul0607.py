class teglalap:
    def __init__(self, hosszusag, szelesseg):
        self.hosszusag = int(hosszusag)
        self.szelesseg = int(szelesseg)
    def kerulet(self):
        return 2 * (self.hosszusag + self.szelesseg)
    def terulet(self):
        return self.szelesseg * self.hosszusag
