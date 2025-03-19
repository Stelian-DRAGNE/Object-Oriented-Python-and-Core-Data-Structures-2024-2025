
## Clasa Paralelogram care are o inaltime si o latime. Calculeaza aria. 
# Spune daca este dreptunghi.
# spunhe daca este romb sau nu.
# Spune daca este patrat sau nu.


class Paralelogram():
    
    def __init__(self, lungime, latime, unghi):
        self.lungime = lungime
        self.latime = latime
        self.unghi = unghi

    def __str__(self):
        return f"{self.forma()} are Lungime: {self.lungime} latime: {self.latime} unghi {self.unghi} are aria {self.aria()}."

    def aria(self):
        return self.lungime * self.latime

    def este_dreptunghi(self):
        return self.unghi == 90

    def este_romb(self):
        return self.latime == self.lungime

    def este_patrat(self):
        return self.este_dreptunghi() and self.este_romb()

    def forma(self):
        if self.este_patrat():
            return "Patrat"
        elif self.este_dreptunghi():
            return "Dreptunghi"
        elif self.este_romb():
            return "Romb"
        else:
            return "Paralelipiped"



print()

paralelogram = Paralelogram(20, 30, 100)
print(paralelogram, "\n")

dreptunghi = Paralelogram(10, 20, 90)
print(dreptunghi, "\n")

romb = Paralelogram(40, 40, 40)
print(romb, "\n")

patrat = Paralelogram(40, 40, 90)
print(patrat, "\n")