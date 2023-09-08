''' 
Abstract class:
      A class that contains one or more abstract methods is called astract class
      Note:
      An object of an astract class cannot be created.
      Python provides abc(pre-defined) module that works with abstration
      We use @abstractmethod decorator to define abstract method
      @abstractmethod decorator is used when we have common action but d/f implimentation
Syntax:
  From abc(module) import ABC(class)
  class demo(ABC):
      def fun(self):
          body
    @abstractmethod
    def fun2(self):              It has no body.Its implimentation is in child class 
'''
from abc import ABC,abstractmethod
class car(ABC):
    def show(self):
        print("Car has 4 wheels")
    @abstractmethod
    def speed(self):
        pass
class Maruthi(car):
    def speed(self):
        print("Maruthi runs at 100km/h")
class Suzuki(car):
    def speed(self):
        print("Suzuki runs at 70km/h")
obj = Maruthi()
obj.show()
obj.speed()

obj1 = Suzuki()
obj1.show()
obj1.speed()    

# obj3 = car()         #Cannot create object for the abstract class and call the functions 
# obj3.show()            
# obj3.speed()

