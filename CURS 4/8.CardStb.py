
""" 

    Trebuie creaya clasa StbCard care reprezinta cardul de la regia autonoma de transport.
    Atributele necesare sunt : mumele detinatorului, calatorii disponibile si creditul disponibil.
    In cazul in care nu primeste numele detinatorului, stati-l automat pe "Nenominal".
    Setati valoarea unei calatorii validate cu credit 3 lei.
    Creati functii automate pentru validare cu credit/validare calatorie si reincarcare credit/reincarcare calatorii.

"""


class StbCard:
    VALOARE_CALATORIE = 3
    def __init__(self, nume = "Nenominal", calatorii = 0, credit = 0):
        self.nume = nume
        self.calatorii = calatorii
        self.credit = credit

    def __str__(self):
        return f"{self.nume} are {self.calatorii} calatorii si {self.credit} lei credit."

    def validare_calatorie(self):
        if self.calatorii:
            self.calatorii -=1
        elif self.credit >= StbCard.VALOARE_CALATORIE:
            self.credit -= StbCard.VALOARE_CALATORIE
        else:
            print("Mergi pe blat !!!")

    def reincarcare_calatorii(self, calatorii_noi):
        self.calatorii = calatorii_noi

    def reincarcare_credit(self, credit):
        self.credit += credit

    def reincarcare(self, **kargs):
        self.calatorii += kargs.get("calatorii", 0)
        self.credit += kargs.get("credit", 0)

    def reincarcare_2(self, credit = 0, calatorii_noi = 0):
        self.credit += credit
        self.calatorii = calatorii_noi



card1 = StbCard("Ion Ionescu", 3, 3)
print(card1)

card2 = StbCard()
print(card2)

card3 = StbCard(credit = 4)
print(card3)

card1.validare_calatorie()
print(card1)
card1.validare_calatorie()
print(card1)
card1.validare_calatorie()
print(card1)
card1.validare_calatorie()
print(card1)
card1.validare_calatorie()
print(card1)


card1.reincarcare(credit = 10)
card1.reincarcare(calatorii = 7)
print(card1)
card1.reincarcare(calatorii = 1, credit = 1)
print(card1)

card1.reincarcare()
print(card1)


card2.reincarcare_2(calatorii_noi = 1, credit = 1)
print(card2)