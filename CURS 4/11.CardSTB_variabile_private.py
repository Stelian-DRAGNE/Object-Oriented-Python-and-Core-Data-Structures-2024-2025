
class CardSTB:
    VALOARE_CALATORIE = 3
    def __init__(self, nume = "Nenominal", calatorii = 0, credit = 0):
        self.__nume = nume
        self.__calatorii = calatorii
        self.__credit = credit

    def __str__(self):
        return f"{self.__nume} are {self.__calatorii} calatorii si {self.__credit} lei credit."

    def get_nume(self):
        return self.__nume

    @property
    def nume(self):
        return self.__nume

    @property
    def calatorii(self):
        return self.__calatorii

    def set_nume(self, nume_nou):
        if isinstance(nume_nou, str):
            self.__nume = nume_nou

    @nume.setter
    def nume(self, nume_nou):
        if isinstance(nume_nou, str):
            self.__nume = nume_nou

    @calatorii.setter
    def calatorii(self, valoare_noua):
        if isinstance(valoare_noua, int) and valoare_noua >= 0:
            self.__calatorii = valoare_noua



card = CardSTB("Ion Ionescu", 3, 5)
print(card)

print(card._CardSTB__nume)
print(card.get_nume())

card.set_nume("Altcineva.")
print(card.get_nume())

card.set_nume([3, 5, 32])
print(card.get_nume())

print(card.nume)

card.nume = [321, 4, 12, 412]
print(card.nume)

card.nume = "Hello"
print(card.nume)

card.nume = ["Hello", "32"]
print(card.nume)

print(card.calatorii)
card.calatorii = "Infinit"
print(card.calatorii)

card.calatorii = 30
print(card.calatorii)
card.calatorii = -30
print(card.calatorii)