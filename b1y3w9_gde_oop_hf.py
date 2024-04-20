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