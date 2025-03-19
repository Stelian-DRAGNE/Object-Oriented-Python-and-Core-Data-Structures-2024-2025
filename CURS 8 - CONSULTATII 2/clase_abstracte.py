
import abc

class Animal(abc.ABC):
    def __init__(self, nume):
        self.nume = nume

    @abc.abstractmethod
    def sunet(self):
        pass

class Caine(Animal):
    def sunet(self):
        print("ham ham")

class Pisica(Animal):
    def sunet(self):
        print("miau miau")


if __name__ == "__main__":
    
    spike = Caine("Spike")
    spike.sunet()

    tom = Caine("Tom")
    tom.sunet()