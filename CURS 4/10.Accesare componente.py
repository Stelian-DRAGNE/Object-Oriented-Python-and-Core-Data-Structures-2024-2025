
class Telefon:
    def __init__(self, anul_fabricatiei, memorie, imei):
        # ATRIBUT PUBLIC
        self.memorie = memorie

        # ATRIBUT INTERN / PROTECTED
        self._anul_fabricatiei = anul_fabricatiei

        # ATRIBUT PRIVAT
        self.__imei = imei


# EXTERIORUL CLASEI
telefon1 = Telefon(2020, 256, 456987)
print(telefon1._anul_fabricatiei)

telefon1._anul_fabricatiei = "Inaintea erei noastre."
print(telefon1._anul_fabricatiei)


print(telefon1._Telefon__imei)

telefon1._Telefon__imei = "Alta valoare."
print(telefon1._Telefon__imei)