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