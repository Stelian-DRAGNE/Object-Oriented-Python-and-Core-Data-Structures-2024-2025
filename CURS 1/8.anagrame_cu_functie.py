
def sunt_anagrame(cuv1, cuv2):
    if len(cuv1) != len(cuv2):
        # Dictionar cu cheie litere si valoare numar de iteratii
        return False

    dict_cuv1 = {}
    for ch in cuv1:
        dict_cuv1[ch] = dict_cuv1.get(ch, 0) + 1
    
    dict_cuv2 = {}
    for ch in cuv2:
        dict_cuv2[ch] = dict_cuv2.get(ch, 0) + 1

    if dict_cuv1 == dict_cuv2:
        return True
    else:
        return False

print(sunt_anagrame("maro", "roma"))
print(sunt_anagrame("maro", "romar"))