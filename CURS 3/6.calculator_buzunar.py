
class CalculatorBuzunar:
    def __init__(self):
        self.total = 0

    def __str__(self):
        return f"{self.total}"

    def add(self, valoare):
        self.total += valoare

    def sub(self, valoare):
        self.total -= valoare

    def mul(self, valoare):
        self.total *= valoare

    def div(self, valoare):
        self.total /= valoare


calc = CalculatorBuzunar()
print(calc)

calc.add(30)
print(calc)

calc.add(30)
print(calc)

calc.div(3)
print(calc)

calc.sub(10)
print(calc)

calc.mul(1.5)
print(calc)