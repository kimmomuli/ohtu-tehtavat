from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from stub_io import StubIO

class Komentotehdas:
    def pelaaja_vs_pelaaja(self):
        stub_io = StubIO()
        return KPSPelaajaVsPelaaja(stub_io)

    def tekoaly(self):
        return KPSTekoaly(StubIO())

    def parempi_tekoaly(self):
        return KPSParempiTekoaly(StubIO())