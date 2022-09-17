class Cat:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def info(self):
        print("I am a Cat.My name is " + str((self.name)))
        print(f"i am {self.age} years old")
    def make_sound(self):
        print("meow")

class Cow:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def info(self):
        print(f"I am a Cow. My name is {self.name}. I am {self.age} years old")
    def make_sound(self):
        print("Moo")

c1=Cat("pussy",3)
c2=Cow("snowy",6)

for animal in (c1,c2):
    animal.make_sound()
    animal.info()
    animal.make_sound()
    print("------------------------------")


