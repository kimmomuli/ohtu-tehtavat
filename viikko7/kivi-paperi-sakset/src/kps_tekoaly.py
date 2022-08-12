from kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self, stub_io):
        super().__init__(stub_io)
        self.tekoaly = Tekoaly()

    def pelaa(self):
        super().pelaa()

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.tekoaly.anna_siirto()
