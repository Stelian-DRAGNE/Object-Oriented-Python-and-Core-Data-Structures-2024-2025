
class CalculatorBuzunar:
    def __init__(self):
        self.total = 0

    def __str__(self):
        return f"{self.total}"

    def __iadd__(self, valoare):
        self.total += valoare
        return self

    def add(self, valoare):
        self.total += valoare

    def __isub__(self, valoare):
        self.total -= valoare
        return self

    def sub(self, valoare):
        self.total -= valoare

    def __imul__(self, valoare):
        self.total *= valoare
        return self

    def mul(self, valoare):
        self.total *= valoare

    def __truediv__(self, valoare):
        self.total /= valoare
        return self

    def div(self, valoare):
        self.total /= valoare


calc = CalculatorBuzunar()
calc += 2
print(calc)

calc -= 4
print(calc)

calc *= 5
print(calc)

calc /= 5
print(calc)