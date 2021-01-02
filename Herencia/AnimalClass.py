# ejemplo de herencia
class Animal:

    def __init__(self):
        self.animalType=""

    def getType(self):
        return  self.animalType

    def setType(self, type):
        self.animalType = type


# de esta manera se define la herencia
class Dog(Animal):

    def __init__(self):
        self.setType("Mammal")


# si no se define nada en la clase se agrega la plabra pass
class Cat(Animal):
    pass




dog1 = Dog()
cat = Cat()
cat.setType("Mammal")
print(dog1.getType())
print(cat.getType())
