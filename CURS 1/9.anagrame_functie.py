
def sunt_anagrame(cuv1, cuv2):
    list_cuv1 = list(cuv1)
    list_cuv2 = list(cuv2)
    list_cuv1.sort()
    list_cuv2.sort()
    return list_cuv1 == list_cuv2

print(sunt_anagrame("maro", "roma"))
print(sunt_anagrame("maro", "romar"))