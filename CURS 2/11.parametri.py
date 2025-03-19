
def sorteaza(*valori):
    lista_sortata = []
    for cuv in valori:
        # Cand lista este goala
        for cuv_existent in lista_sortata:
            if cuv < cuv_existent:
                lista_sortata.insert(lista_sortata.index(cuv_existent), cuv)
                break
        else:
            lista_sortata.append(cuv)
    return lista_sortata

print(sorteaza("verde", "negru", "alb", "gri", "fuchsia"))
print(sorteaza(421, 32, 22, 22, 109, 2230, 30, 1123, 32))