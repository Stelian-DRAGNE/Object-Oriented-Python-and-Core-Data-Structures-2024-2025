
def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    return a / b

def calculeaza(a, b, func):
    return func(a, b)


## Programare functionala
print(calculeaza(5, 10, inmultire))
print(calculeaza(1, 123, adunare))
print(calculeaza(10, 2, impartire))
print(calculeaza(10, 2, scadere))

print(calculeaza(5, 10, inmultire), calculeaza(1, 123, adunare), calculeaza(10, 2, impartire), calculeaza(10, 2, scadere))