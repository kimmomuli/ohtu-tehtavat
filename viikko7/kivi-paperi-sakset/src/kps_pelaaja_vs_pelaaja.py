from kps import KPS

class KPSPelaajaVsPelaaja(KPS):
    def __init__(self, stub_io):
        super().__init__(stub_io)

    def pelaa(self):
        super().pelaa()
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.stub_io.lue("Toisen pelaajan siirto: ")

    def _tulosta_siirto(self, tokan_siirto):
        return

