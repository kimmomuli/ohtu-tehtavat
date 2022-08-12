from stub_io import StubIO
from komentotehdas import Komentotehdas

def main():
    io = StubIO()
    komentotehdas = Komentotehdas()
    while True:
        io.print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = io.lue('')

        if vastaus.endswith("a"):
            io.print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = komentotehdas.pelaaja_vs_pelaaja()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            io.print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = komentotehdas.tekoaly()
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            io.print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = komentotehdas.parempi_tekoaly()
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
