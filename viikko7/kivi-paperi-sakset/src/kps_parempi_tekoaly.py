from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self, stub_io):
        super().__init__(stub_io)
        self.parempi_tekoaly = TekoalyParannettu(10)

    def pelaa(self):
        super().pelaa()

    def _toisen_siirto(self, ekan_siirto):
        return self.parempi_tekoaly.anna_siirto()
    
    def aseta_siirto(self, ekan_siirto):
        return self.parempi_tekoaly.aseta_siirto(ekan_siirto)

