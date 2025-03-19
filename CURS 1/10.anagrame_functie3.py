
print(sorted("maro"), type(sorted("maro")))
print(sorted("maro"))

def sunt_anagrame(cuv1, cuv2):
    return sorted(cuv1) == sorted(cuv2)

print(sunt_anagrame("maro", "roma"))
print(sunt_anagrame("maro", "romar"))