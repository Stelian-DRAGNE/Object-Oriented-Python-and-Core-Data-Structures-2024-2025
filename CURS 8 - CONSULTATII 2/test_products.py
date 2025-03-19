
from Shop.products import Produs
from Shop.parfumuri import Parfum
from Shop.comanda import Comanda

try:
    p1 = Produs("err", "lorem ipsum ...", 60)
    print(p1.nume)
except:
    print("Produsul nu poate fi instantiat (CLASA ABSTRACTA).")


stronger = Parfum("Stronger with you", "Poate contine urma de parfum", 1000, 100)
print(stronger.pret)
# stronger.discount(0.5)
print(stronger.pret)


comanda = Comanda(stronger, stronger)
print(comanda.total)

comanda += stronger
print(comanda.total)

# p2 = Produs("Rosu")
# print(p2.id)

# Produs.CONTOR = 5

# p3 = Produs("Negru")
# print(p3.id)

# p3.nume = "*"
# print(p3.nume)

# valoare = 3