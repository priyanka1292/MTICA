class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grrr.....")

class Dog(Wolf):
    def bark(self):
        print("Woof")

pet1=Dog("tommy","brown")

pet1.bark()
pet2=Wolf("jimmy","grey")
pet2.bark()
Dog("abc","xyz").bark()

#redefining a method of base class in derived class is overloading
