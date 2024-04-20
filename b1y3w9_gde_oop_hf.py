from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def get_szobatipus(self):
        pass


class EgyagyasSzoba(Szoba):
    def get_szobatipus(self):
        return "Egyágyas"


class KetagyasSzoba(Szoba):
    def get_szobatipus(self):
        return "Kétágyas"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas_felvetel(self, foglalas):
        self.foglalasok.append(foglalas)

    def foglalas_lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            print("Foglalás sikeresen törölve.")
        else:
            print("Nincs ilyen foglalás.")

    def foglalasok_listazasa(self):
        print("Foglalások:")
        for foglalas in self.foglalasok:
            print(foglalas)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Szoba: {self.szoba.szobaszam}, Dátum: {self.datum}"

def main():
    # Szálloda létrehozása
    szalloda = Szalloda("Példa Szálloda")

    # Szobák létrehozása és hozzáadása a szállodához
    egyagyas_szoba1 = EgyagyasSzoba("101", 5000)
    ketagyas_szoba1 = KetagyasSzoba("202", 8000)
    ketagyas_szoba2 = KetagyasSzoba("203", 8100)

    szalloda.szoba_hozzaad(egyagyas_szoba1)
    szalloda.szoba_hozzaad(ketagyas_szoba1)
    szalloda.szoba_hozzaad(ketagyas_szoba2)

    # Foglalások létrehozása és hozzáadása a szállodához
    foglalas1 = Foglalas(egyagyas_szoba1, datetime(2024, 4, 1))
    foglalas2 = Foglalas(ketagyas_szoba1, datetime(2024, 4, 3))
    foglalas3 = Foglalas(ketagyas_szoba1, datetime(2024, 5, 3))

    szalloda.foglalasok = [foglalas1, foglalas2, foglalas3]


# Felhasználói interfész
    while True:
        print("\n1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Válasszon egy műveletet: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a szobaszámot: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            # Szoba ellenőrzése
            for szoba in szalloda.szobak:
                if szoba.szobaszam == szobaszam:
                    # Dátum ellenőrzése
                    if datum < datetime.now():
                        print("Érvénytelen dátum! Kérem adjon meg jövőbeli dátumot.")
                        break
                    foglalas = Foglalas(szoba, datum)
                    szalloda.foglalas_felvetel(foglalas)
                    print("Foglalás sikeresen rögzítve.")
                    break
            else:
                print("Nincs ilyen szoba.")

        elif valasztas == "2":
            szobaszam = input("Adja meg a szobaszámot: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            for foglalas in szalloda.foglalasok:
                if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                    szalloda.foglalas_lemondas(foglalas)
                    break
            else:
                print("Nincs ilyen foglalás.")

        elif valasztas == "3":
            szalloda.foglalasok_listazasa()

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")


if __name__ == "__main__":
    main()