
# Numele clasei este intotdeauna cu litera mare
class Animal:

    def __init__(self, nume, varsta):
        print("__init__ din Animal este chemata.")
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f'{type(self).__name__} {self.nume} are {self.varsta} an{"i" if self.varsta != 1 else ""}'


class Pisica(Animal):
    def __init__(self, nume, varsta, culoare):
        print("__init__ din Pisica este chemata.")
        super().__init__(nume, varsta)
        self.culoare = culoare

    def miauna(self):
        print("miau")

    ## Suprascrierea metodei __str__
    def __str__(self):
        return f'{super().__str__()} si are culoarea {self.culoare}'

class PisicaBirmaneza(Pisica):
    def __init__(self, nume, varsta, culoare, dragalasenie):
        print("__init__ din PisicaBirmaneza este chemata.")
        super().__init__(nume, varsta, culoare)
        self.dragalasenie = dragalasenie

    def __str__(self):
        return f'{super().__str__()} si are dragalasenie {self.dragalasenie}.'

class Caine(Animal):
    pass

# Conditie prin care verific ca rulez codul direct din acest fisier
if __name__ == "__main__":
    obj_animal = Animal("Gigi", 1)
    print(obj_animal)
    # obj_pisica.miauna() - Nu pot chema functia 'miauna', deoarece ace afunctie nu exista pentru clasa 'Animal'

    obj_animal = Animal("Gigi", 11)
    print(obj_animal)
    # obj_pisica.miauna() - Nu pot chema functia 'miauna', deoarece ace afunctie nu exista pentru clasa 'Animal'

    obj_pisica = Pisica("Rino", 5.5)
    print(obj_pisica)
    obj_pisica.miauna()

    obj_caine = Caine("Spike", 2)
    print(obj_caine)
    # obj_pisica.miauna() - Nu pot chema functia 'miauna', deoarece ace afunctie nu exista pentru clasa 'Caine'