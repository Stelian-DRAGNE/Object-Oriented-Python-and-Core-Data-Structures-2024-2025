
class Calcul:
    def __init__(self, valoare_finala):
        self.vf = valoare_finala

    def __str__(self):
        return f"{self.vf * 100 / 89}"


print(Calcul(100))