class Wolf:
    price=400
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grrrr....")

class Dog(Wolf):
    def bark1(self):
        print("Wolf")
if __name__=="__main__":
    pet1=Dog("tommy","brown")
    pet1.bark()
    pet1.bark1()
    print(pet1.name," is of color ",pet1.color)
