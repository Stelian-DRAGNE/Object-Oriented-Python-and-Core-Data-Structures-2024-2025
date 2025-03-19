
def pozitive(functie):
    def inner_func(a, b):
        if a < 0 or b < 0:
            return "Calculul nu poate fi facut fiindca avem valori negative."
        else:
            return f"Rezultatul este: {functie(a, b)}"
    return inner_func


@pozitive
def adunare(a, b):
    return a + b

@pozitive
def scadere(a, b):
    return a - b

@pozitive
def inmultire(a, b):
    return a * b

@pozitive
def impartire(a, b):
    return a / b

print(adunare(1, 2))
print(adunare(1, -2))