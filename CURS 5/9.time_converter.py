
"""

1. Creati clasa TimeConverter cu doua proprietati(atribute):
    hours - numarul de ore (int)
    minutes - numarul de minute (int)

2. Clasa trebuie sa contina urmatoarele metode publice :
    - toMinutes() - converteste timpul total in minute 
    - toHours() - converteste timpul total in ore
    - addTime() - aduna inca un interval de timp si returneaza rezultatul in minute
    - diffTime() - calculeaza diferenta fata de alt interval de timp si returneaza rezultatul in minute.

"""


class TimeConverter:
    def __init__(self, hours, minutes):
        self.__hours = hours
        self.__minutes = minutes

    @property
    def h(self):
        return self.__hours

    @h.setter
    def h(self, new_value):
        if isinstance(new_value, int) and new_value >= 0:
            self.__hours = new_value

    @property
    def m(self):
        return self.__minutes

    @m.setter
    def m(self, new_value):
        if isinstance(new_value, int) and new_value >= 0:
            self.__minutes = new_value % 60
            self.h += new_value // 60

    def __str__(self):
        return f"{self.h} ore si {self.m} minute."

    def toMinutes(self):
        return self.h * 60 + self.m

    @property
    def total_minutes(self):
         return self.h * 60 + self.m 

    def toHours(self):
        return round(self.h + self.m / 60, 2)

    @property
    def total_hours(self):
        return round(self.h + self.m / 60, 2) 

    def addTime(self, other_tc):
        self.h += other_tc.h
        self.m += other_tc.m

    def diffTime(self, other_tc):
        self.h -= other_tc.h
        if self.m >= other_tc.m:
            self.m -= other_tc.m
        else:
            self.m = (60 + self.m - other_tc.m)
            self.h -= 1


tc = TimeConverter(6, 30)
print(tc)
print(tc.toMinutes(), "minute.")
print(tc.total_minutes, "minute.")
print(tc.toHours())
print(tc.total_hours)


tc2 = TimeConverter(1, 33)
tc.diffTime(tc2)
print(tc)