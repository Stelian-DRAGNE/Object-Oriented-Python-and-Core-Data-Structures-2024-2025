
# •   Construiti clasa Account(cont bancar) care sa abstractizeze un cont bancar
# •   Clasa deţine următoarele implementari cu verificarile necesare:
#     o widthdraw(scoateBani) - se scot bani din portofel
#     o addMoney(adaugaBani)  - se adaga bani in portofel
#     o showBalance(arataBalanta) - se printeaza balanta curenta


class Account:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"Contul are {self.balance} lei."

    def withdraw(self, suma):
        if suma > self.balance:
            print("Fonduri insuficiente.")
        else:
            self.balance -= suma

    def add_money(self, suma):
        if suma < 0:
            print("Nu se poate asa ceva ...")
        else:
            self.balance += suma

    def show_balance(self):
        print(self)


cont1 = Account(10)
print(cont1)
cont1.withdraw(11)
print(cont1)

cont1.add_money(20)
print(cont1)

cont1.add_money(-3)

cont1.show_balance()

# cont2 = Account(33)
# print(cont2)
