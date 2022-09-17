from abc import ABC,abstractmethod
class Animal(ABC):
    def sleep(self):
        print("i am going to sleep in a while")

    @abstractmethod
    def sound(self):
        print("this function is for defining the sound by any animal")
    pass

class Snake(Animal):
    def sound(self):
        print("I can hiss")

class Dog(Animal):
    def sound(self):
        print("I can bark")

class Lion(Animal):
    def sound(self):
        print("I can roar")

class Cat(Animal):
    def sound(self):
        print("I can meow")

class Deer(Animal):
    def sound(self):
        pass

c=Snake()
c.sound()

c=Dog()
c.sound()

c=Lion()
c.sound()

c=Cat()
c.sound()
''' If we want to acces the sound() function of the base class itself,
we can use the object of the child class, but we will have to invoke it through
super().'''

class Rabbit(Animal):
    def sound(self):
        super().sound()
        print("I can squeak")
c = Rabbit()
c.sound()