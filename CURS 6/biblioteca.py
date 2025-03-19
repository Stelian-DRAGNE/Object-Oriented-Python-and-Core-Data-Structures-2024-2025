
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

class Book:
    def __init__(self, titlu, autor = "Necunoscut"):
        self.__titlu = titlu
        self.__autor = autor

    def __str__(self):
        return self.__titlu

    ## obiect1 == obiect2
    def __eq__(self, other):
        return self.__titlu == other.__titlu and self.__autor == other.__autor

class Library:
    # ARE - Biblioteca are carti
    def __init__(self, *books):
        self.__books = list(books)

    def __str__(self):
        return " - ".join([str(book) for book in self.__books])

    # library += book
    def __iadd__(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
        return self

    # library -= book
    def __isub__(self, book):
        if isinstance(book, Book) and book in self.__books:
            self.__books.remove(book)
        return self
    @property
    def books(self):
        return self.__books


b1 = Book("Python 3 Object Oriented Programming")
b2 = Book("Python 3 in 1")
b3 = Book("Python Cookbook")

library = Library(b1, b2, b3)
print(library)

b4 = Book("Everything Python")
library += b4
print(library)

library -= b3
print(library)\

b5 = Book("Python 3 Object Oriented Programming")
library -= b5
print(library)


print(b1 == b5)
print("b1 = ", b1)
print("b5 = ", b5)