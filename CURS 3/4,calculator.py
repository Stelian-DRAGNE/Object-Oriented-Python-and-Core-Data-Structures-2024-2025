
class Calculator():
    def __init__(self, operand1, operand2):
        self.op1 = operand1
        self.op2 = operand2

    def __str__(self):
        return f"Calcul cu {self.op1} si {self.op2}"

    def add(self):
        return self.op1 + self.op2

    def sub(self):
        return self.op1 - self.op2

    def mul(self):
        return self.op1 * self.op2

    def div(self):
        return self.op1 / self.op2





calc = Calculator(10, 5)
print(calc)

print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())