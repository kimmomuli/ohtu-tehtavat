class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.luku_jono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.luku_jono

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
            
        self.luku_jono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        if self.alkioiden_lkm == len(self.luku_jono):
            self.luku_jono += self.kasvatuskoko * [0]

        return True


    def poista(self, n):
        if self.kuuluu(n):
            self.luku_jono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [luku for luku in self.luku_jono if luku != 0]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            x.lisaa(luku)

        for luku in b_taulu:
            x.lisaa(luku)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku in b_taulu:
                y.lisaa(luku)

        return y

    @staticmethod
    def erotus(a, b):
        palautettava_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku not in b_taulu:
                palautettava_joukko.lisaa(luku)

        return palautettava_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"

        elif self.alkioiden_lkm == 1:
            return "{" + str(self.luku_jono[0]) + "}"
            
        else:
            tuotos = ""
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + f"{self.luku_jono[i]}, "

            tuotos = tuotos + str(self.luku_jono[self.alkioiden_lkm - 1])
            return f"{{{tuotos}}}"
