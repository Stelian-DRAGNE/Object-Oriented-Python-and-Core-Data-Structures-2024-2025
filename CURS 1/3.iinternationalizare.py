
lang = input("Choose your language (ro/en/it):")

while lang not in ["ro", "en", "it"]:
    lang = input("Please choose from ro/en/it :")

traduceri = {
    "ro" : ("Introduceti priumul numar: ", "Introduceti doar numere.", "Introduceti al doilea numar: ", "Alegeti operatia (+, -, *, /)", "Rezultatul este: "),
    "en" : ("Insert first number: ", "Insert only numbers.", "Insert the second number: ", "Choose operation (+, -, *, /)", "The result is: "),
    "it" : ("Inserire il primo numero: ", "Inserisci solo numeri.", "Inserire il secondo numero: ", "Scegli l'operatione (+, -, *, /)", "Il resultato è: "),
}

no1 = input(traduceri[lang][0])
while not no1.isnumeric():
    no1 = input(traduceri[lang][1])
no1 = int(no1)
print(no1)

no2 = input(traduceri[lang][2])
while not no2.isnumeric:
    no2 = input(traduceri[lang][1])
no2 = int(no2)
print(no2)

op = input(traduceri[lang][3])

rezultat = no1 + no2
print(traduceri[lang][4], rezultat)