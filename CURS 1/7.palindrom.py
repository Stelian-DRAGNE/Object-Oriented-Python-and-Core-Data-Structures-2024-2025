
def este_palindrom(cuv):
    for i in range(len(cuv)):
        if cuv[i] != cuv[-1 -i]:
            print("Cuvantul nu este palindrom.")
            break
    else:
        print("Cuvantul este palindrom.")

cuvant = "caimac"
rezultat = este_palindrom(cuvant)
print(rezultat)