

def este_palindrom(cuv):
    for i in range(len(cuv)):
        if cuv[i] != cuv[-1 -i]:
            return False, cuv
    return True, cuv

cuvant = "caimac"
rezultat = este_palindrom(cuvant)
print(rezultat)

print(este_palindrom("tractor"))
print(este_palindrom("level"))
print(este_palindrom("minim"))
print(este_palindrom("civic"))
print(este_palindrom("radar"))
print(este_palindrom("gigi"))