
from Shop.products import Produs

class Parfum(Produs):
    CANTITATE_MINIMA = 25
    def __init__(self, nume:str, descriere:str, pret:int, cantitate:int):
        super().__init__(nume, descriere, pret)

        if isinstance(cantitate, int) and cantitate >= Parfum.CANTITATE_MINIMA:
            self._cantitate = cantitate
        else:
            raise ValueError(f"Cantitatea trebuie sa fie mai mare ca {Parfum.CANTITATE_MINIMA}.")

    def discount(self, valoare = 0.82):
        """ reducere de 18% """
        self.pret = int(self.pret * valoare)