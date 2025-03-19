
traduceri = {
    "ro" : {
        "no1" : "Introduceti priumul numar: ", 
        "numeric" : "Introduceti doar numere.", 
        "no2" : "Introduceti al doilea numar: ",
        "op" : "Alegeti operatia (+, -, *, /)",
        "re_op" : "Alegeti doar din +, -, *, /",
        "rez" : "Rezultatul este: "},
    "en" : {
        "no1" : "Insert first number: ", 
        "numeric" : "Insert only numbers.", 
        "no2" : "Insert the second number: ",
        "op" : "Choose operation (+, -, *, /)",
        "re_op" : "Choose only from +, -, *, /",
        "rez" : "The result is: "},
    "it" : {
        "no1" : "Inserire il primo numero: ", 
        "numeric" : "Inserisci solo numeri.",
        "no2" : "Inserire il secondo numero: ",
        "op" : "Scegli l'operatione (+, -, *, /)",
        "re_op" : "Scegli solo tra +, -, *, /",
        "rez" : "Il resultato è: "},
    "de" : {
        "no1" : "Erste Zahl einfügen:", 
        "numerisch" : "Nur Zahlen einfügen.", 
        "no2" : "Fügen Sie die zweite Zahl ein:",
        "op": "Operation auswählen (+, -, *, /)",
        "re_op": "Nur aus +, -, *, / wählen",
        "rez": "Das Ergebnis ist: "},
    "fr" : {
        "no1" : "Entrez le premier chiffre : ", 
        "numeric" : "Entrez uniquement des chiffres.", 
        "no2" : "Entrez le deuxième numéro : ",
        "op" : "Choisir l'opération (+, -, *, /)",
        "re_op" : "Choisissez uniquement parmi +, -, *, /",
        "rez" : "Le résultat est : "},
    }

lang = input(f"Choose your language {list(traduceri.keys())}:")

while lang not in traduceri.keys():
    lang = input(f"Please choose from {list(traduceri.keys())}:")

no1 = input(traduceri[lang]["no1"])
while not no1.isnumeric():
    no1 = input(traduceri[lang]["numeric"])
no1 = int(no1)
print(no1)

no2 = input(traduceri[lang]["no2"])
while not no2.isnumeric:
    no2 = input(traduceri[lang]["numeric"])
no2 = int(no2)
print(no2)

op = input(traduceri[lang]["op"])
while op not in ("+", "-", "*", "/"):
    op = input(traduceri[lang]["re_op"])

if op == "+":
    rezultat = no1 + no2
elif op == "-":
    rezultat = no1 - no2
elif op == "*":
    rezultat = no1 * no2
elif op == "/":
    rezultat = no1 / no2
print(traduceri[lang]["rez"], rezultat)