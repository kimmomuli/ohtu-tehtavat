from tuomari import Tuomari

class KPS:
    def __init__(self, stub_io):
        self.stub_io = stub_io

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)
        self._tulosta_siirto(tokan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            self._tulosta_siirto(tokan_siirto)
            self.aseta_siirto(ekan_siirto)

        self.stub_io.print("Kiitos!")
        print(tuomari)

    def aseta_siirto(self, ekan_siirto):
        return

    def _tulosta_siirto(self, tokan_siirto):
        self.stub_io.print(f"Tietokone valitsi: {tokan_siirto}")

    def _ensimmaisen_siirto(self):
        return self.stub_io.lue("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        return

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"