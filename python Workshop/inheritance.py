class person(object):
    def __init__(self,name,id_n):
        self.name= name
        self.id_n= id_n

    def Display(self):
        print(self.name,self.id_n)

v=person("vsm",12)
print("my name is=",v.name)
print("id=",v.id_n)

class abc(person):
    def printabc(self):
        print("abc class called")

mvs= abc("aditya",13)
mvs.Display()
mvs.printabc()

