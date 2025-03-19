
def este_palindrom(cuvant):
    return cuvant == cuvant[::-1]

print(este_palindrom("caiac"))
print(este_palindrom("maro"))

def este_palindrom_v2(cuvant):
    return list(cuvant) == list(reversed(cuvant))

print(este_palindrom_v2("caiac"))
print(este_palindrom_v2("maro"))