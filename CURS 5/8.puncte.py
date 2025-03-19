
"""

Trebuie creată clasa Point care sa abstractizeze un punct dintr-un plan (coordonate x si y)
Clasa deţine următoarele caracteristici:
    • Punctul x si punctul y
Clasa deţine următoarele implementari:
    o show - se printeaza coordinatele punctului;
    o move - se muta coordonatele;
    o setToOrigin - se seteaza coordinatele (0, 0);
    o dist - distanta intre doua puncte

"""

from math import sqrt as radical

class Point:
    def __init__(self, x, y):
        # Private
        self.__coord_x = x
        self.__coord_y = y

    @property
    def x(self):
        return self.__coord_x

    @x.setter
    def x(self, new_x):
        if isinstance(new_x, int):
            self.__coord_x = new_x

    @property
    def y(self):
        return self.__coord_y

    @y.setter
    def y(self, new_y):
        if isinstance(new_y, int):
            self.__coord_y = new_y

    def __str__(self):
        return f"({self.x},{self.y})"

    def show(self):
        print(self)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def set_to_origin(self):
        self.x = 0
        self.y = 0

    def distance(self, other):
        return radical((self.x - other.x) ** 2 + (self.y - other.y) ** 2)



p1 = Point(2, 3)
print(p1)
p1.show()


p1.x = 36
print(p1)
p1.x = "jhjhjhjh"
print(p1)


p1.set_to_origin()
print(p1)

p2 = Point(3, 4)
print(p1.distance(p2))
print(p2.distance(p1))