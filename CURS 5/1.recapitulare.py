
# Definirea clasei
class Curs:
    def __init__(self, nume):
        self.__nume = nume

    def __str__(self):
        return f"Cursul {self.__nume}"
    
    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, new_value):
        if type(new_value) == str and len(new_value) > 1:
            self.__nume__ = new_value        


obiect_de_tip_curs = Curs("OOP")
print(obiect_de_tip_curs)

# Name mangling
print(obiect_de_tip_curs._Curs__nume)
print(obiect_de_tip_curs.nume)

obiect_de_tip_curs.nume = "_"
print(obiect_de_tip_curs.nume)