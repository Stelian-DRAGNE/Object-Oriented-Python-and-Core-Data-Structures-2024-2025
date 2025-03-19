

class ProcesatorText:
    def __init__(self, text, vocale):
        self.text = text
        self.vocale = vocale

    def __str__(self):
        return self.text

    def elimina_vocale(self):
        rezultat = ""
        for i in self.text:
            if i not in self.vocale:
                rezultat +=i
        return rezultat

procesator = ProcesatorText("La multi ani !!!", "aeiouAEIOU")
print(procesator)

print(procesator.elimina_vocale())
print(procesator.elimina_vocale())