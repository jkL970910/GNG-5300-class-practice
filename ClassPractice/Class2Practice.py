# extends ================================
class Vehicle:
 
    def __init__(self):
        print("Vehicle is Ready")
 
    def who_is_this(self):
        print("Vehicle")
 
    def engine_start(self):
        print("start engine")
 
class Truck(Vehicle):   # write Child(Parent) as extend
 
    def __init__(self):
        super().__init__()   # extend parent init will call the functions inside the parent constructor
        print("Truck is Ready") 
 
    def who_is_this(self):  # child function will override the parent function directly
        print("Truck")
 
    def start(self):
        print("start Truck")
 
a = Truck()
a.who_is_this()
 
# Encapsulation =================================
class Computer:
    def __init__(self):
        self.__maxprice = 900    # use __ at the leftside of a value to set it as private
 
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
 
    def setMaxPrice(self, price):
        self.__maxprice = price
 
c = Computer()
c.sell()
 
c.__maxprice = 1000
c.sell()
 
c.setMaxPrice(1000)
c.sell()
 
# Polymorphism ====================================
class Parrot:
    def fly(self):
        print("I can fly")
 
    def egg(self):
        print("I can't egg")

class Chicken:
    def fly(self):
        print("I can't fly")
 
    def egg(self):
        print("I can egg")

def bird(bird):
    bird.fly()
    bird.egg()

bird(Parrot())
bird(Chicken())