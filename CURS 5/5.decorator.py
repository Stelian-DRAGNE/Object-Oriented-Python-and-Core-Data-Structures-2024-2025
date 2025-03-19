
def scadere(a, b):
    return a - b

def decorator(func):
    return scadere

@decorator
def adunare(a, b):
    return a + b

@decorator
def inmultire(a, b):
    return a * b

print(adunare(2, 3))
print(inmultire(10, 10))
