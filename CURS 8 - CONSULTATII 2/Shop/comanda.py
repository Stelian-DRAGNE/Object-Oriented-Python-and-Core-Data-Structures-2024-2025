
from datetime import datetime


class Comanda:
    def __init__(self, *produse):
        self._produse = list(produse)
        self.__data_crearii = datetime.now()

    @property
    def data_crearii(self):
        return self.__data_crearii

    @property
    def produse(self):
        return self._produse

    @property
    def total(self):
        return sum([prod.pret for prod in self.produse])

    def __iadd__(self, produs):
        self._produse.append(produs)
        return self