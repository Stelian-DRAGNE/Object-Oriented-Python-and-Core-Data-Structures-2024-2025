
import abc

## Definim clasa
class Produs(abc.ABC):
    # Variabila statica
    __CONTOR = 1000

    # TODO
    """
    O descriere 
        minim 10 caractere - va genera o eroare daca e setat gresit 
    pret
        int (mai mare ca 0) - va genera o eroare daca e setat gresit
    """

    def __init__(self, nume:str, descriere:str, pret:int):
        Produs.__CONTOR += 1
        self.__id = Produs.__CONTOR

        # Variabila interna (protected) - va fi folosita in clase derivate
        if isinstance(nume, str) and len(nume) > 2:
            self._nume = nume
        else:
            raise ValueError("Numele trebuie sa fie din cel putin trei caractere.")

        # Variabila interna (protected) - va fi folosita in clase derivate
        if isinstance(descriere, str) and len(descriere) > 9:
            self._descriere = descriere
        else:
            raise ValueError("Descrierea trebuie sa fie din cel putin zece caractere.")

        if isinstance(pret, int) and pret > 0:
            self._pret = pret
        else:
            raise ValueError("Pretul trebuie sa fie mai mare ca zero.")

    # getter
    @property
    def id(self):
        return self.__id

    @property
    def nume(self):
        return self._nume

    @nume.setter
    def nume(self, valoare_noua):
        if isinstance(valoare_noua, str) and len(valoare_noua) > 2:
            self._nume = valoare_noua

    @property
    def descriere(self):
        return self._descriere

    @descriere.setter
    def descriere(self, valoare_noua):
        if isinstance(valoare_noua, str) and len(valoare_noua) > 9:
            self._descriere = valoare_noua

    @property
    def pret(self):
        return self._pret

    @pret.setter
    def pret(self, valoare_noua):
        if isinstance(valoare_noua, int) and valoare_noua > 0:
            self._pret = valoare_noua

    @abc.abstractmethod
    def discount(self):
        pass