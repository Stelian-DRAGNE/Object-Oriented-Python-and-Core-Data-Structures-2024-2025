
def rezultat_frumos(func):
    def o_alta_functie(a, b):
        return f"Rezultatul de {func.__name__} intre {a} si {b} este {func(a,b)}."
    return o_alta_functie 

@rezultat_frumos
def adunare(a, b):
    return a + b

@rezultat_frumos
def scadere(a, b):
    return a - b

@rezultat_frumos
def inmultire(a, b):
    return a * b

@rezultat_frumos
def impartire(a, b):
    return a / b


print(adunare(1, 2))
print(scadere(3, 4))
print(inmultire(5, 6))
print(impartire(10, 2))