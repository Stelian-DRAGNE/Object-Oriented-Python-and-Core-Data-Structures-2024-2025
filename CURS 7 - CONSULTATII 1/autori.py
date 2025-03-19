
"""

Extindeti functionalitatea programului anterior Library (Biblioteca):

Adaugati clasa Autor. Autorul va avea nume, o nationalitate. 

O carte va putea avea un autor unic, necunoscut sau autor multiplu.

Creati o functie care sa filtreze toti autorii romani si una pe toti autorii straini.
Adaugati clasele Roman, LucrareStiintifica si Manual.

"""


import pycountry

class NationalitateNecunoascutaError(Exception):
    def __init__(self, *args):
        super().__init__("Nationalitatea trebuie sa fie de forma RO sau EN sau HU.")

class Autor:
    NUME_NECUNOSCUT = "UNKNOWN"
    NATIONALITATE_NECUNOSCUTA = "UNKNOWN"
    def __init__(self, nume, nationalitate):
        self.__nume = nume
        if nationalitate in Autor.nationalitati():
            self.__nationalitate = nationalitate
        elif nationalitate == Autor.NATIONALITATE_NECUNOSCUTA:
            self.__nationalitate = nationalitate
        else:
            print("Nu exista aceasta nationalitate.")
            # self.__nationalitate = "Necunoscut."
            raise NationalitateNecunoascutaError()

    def __eq__(self, other):
        return self.name == other.name and self.nationalitate == other.nationalitate
    @property
    def name(self):
        return self.__nume

    @property
    def nationalitate(self):
        return self.__nationalitate

    def __str__(self):
        return f"{self.name} din {self.nationalitate}"

    @staticmethod
    def nationalitati():
        return [country.alpha_2 for country in pycountry.countries]

class AutorNecunoscut(Autor):
    def __init__(self):
        super().__init__(Autor.NUME_NECUNOSCUT, Autor.NATIONALITATE_NECUNOSCUTA)


if __name__ == "__main__":
    try:
        autor1 = Autor("Dusty Phillips", "RO")
        print(autor1.name)
        print(autor1)
    except:
        print("Autorul nu a putut fi creat.")
    # print(Autor.nationalitati())