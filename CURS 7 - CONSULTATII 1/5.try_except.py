
x = 10
y = 3


## Tratamentul erorii
try:
    rezultatul = x / y
    print("Rezultatul impartirii este:", rezultatul)
except:
    print("In acest caz exista o eroare.")
finally:
    print("Aceasta linie se cheama oricum.")