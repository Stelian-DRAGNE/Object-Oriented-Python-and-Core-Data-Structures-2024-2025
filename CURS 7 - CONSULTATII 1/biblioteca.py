
"""

Creati un program nu numele Library(Biblioteca)

Programul va afisa la inceput un meniu cu cateva elemente :
    1 - carte noua
    2 - modificare carte
    3 - stergere carte 
    4 - listarea tuturor cartilor
    5 - iesire din program.

Toate cartile se stocheaza in memorie (continutul se sterge cand programul inceteaza sa functioneze).

"""


# https://dontpad.com/biblioteca1

# import autori
# autori.Autor()
# autori.NationalitateNecunoscutaError()

from autori import Autor, AutorNecunoscut

class Book:
    # metoda = o functie a clasei
    # metode magice
    def __init__(self, titlu:str, autor:Autor | list[Autor] = AutorNecunoscut()):
        self.__titlu = titlu
        self.__autor = autor
        
    def __str__(self):
        if isinstance(self.__autor, Autor):
            return f"{self.__titlu} by {self.__autor}"
        else:
            lista_autori = ", ".join([a.name for a in self.__autor])
            return f"{self.__titlu} by {lista_autori}"
    
    ## obiect1 == obiect2
    def __eq__(self, other):
        return self.__titlu == other.__titlu and  self.__autor == other.__autor

class Library:
    # ARE -> biblioteca are carti
    def __init__(self, *books):
        self.__books = list(books)

    def __str__(self):
        return " - ".join([ str(book) for book in self.__books])
    
    # library += book
    def __iadd__(self, new_book:Book):
        if isinstance(new_book, Book):
            self.__books.append(new_book)
        return self

    # library -= book
    def __isub__(self, new_book:Book):
        if isinstance(new_book, Book) and new_book in self.__books:
            self.__books.remove(new_book)
        return self
    
    @property
    def books(self):
        return self.__books


if __name__ == "__main__":
    a1 = Autor("Dusty Phillips", "HU")
    a2 = Autor("Mihai Eminescu", "RO")

    b1 = Book("Python 3 Object Oriented Programming", a1)
    b2 = Book("Python 3 in 1", a2)
    b3 = Book("Pythoon Cookbook", [a1, a2])

    library = Library(b1, b2, b3)
    print(library)

    b4 = Book("Everything Python")
    ## library.__iadd__(b4)
    library += b4
    print(library)

    library -= b3
    print(library)

    b5 = Book("Python 3 Object Oriented Programming")
    ## library.__isub__(b5)
    library -= b5
    print(library)


    print(b1 == b5)
    print("b1 = ", b1)
    print("b5 = ", b5)
