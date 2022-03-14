from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self.ostoskori])

    def hinta(self):
        return sum([ostos.hinta() for ostos in self.ostoskori])

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() in [ostos.tuotteen_nimi() for ostos in self.ostoskori]:
            for ostos in self.ostoskori:
                if ostos.tuotteen_nimi() == lisattava.nimi():
                    ostos.muuta_lukumaaraa(1)
        else:
            self.ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                if ostos.lukumaara() > 1:
                    ostos.muuta_lukumaaraa(-1)
                else:
                    self.ostoskori.remove(ostos)

    def tyhjenna(self):
        self.ostoskori = []

    def ostokset(self):
        return self.ostoskori
