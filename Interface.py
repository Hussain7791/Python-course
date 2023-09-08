''' 
Interface:
It is a type of abstract class that only contains abstract method and not any normal method.
Syntax:
from abc import ABC
class interface_class(ABC):
    @abstractmethod
    def fun(self):
        pass
    @abstractmethod
    def fun2(self):
        pass
class chlid(interface_class):
    It will override both abstract functions of parent class. If any one of them is not overrided then it will become simple abstract class
    Now we can make many more child classes but overriding abstract functions of parent class is compulsory in all child classes we make.
class chlid2(interface_class):
    body
    Note:
    We cannot create object of interface
    We use interface when action is common but implimentation is different 
    All chlid class should inherit abstract methid
'''
# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def show(self):
#         pass
#     # def design(self):
#     #     print("Designing.....")        #This is a normal function so the class is abstract class. By commenting this fun the class will become a interface.
# class square(shape):
#     def show(self):
#         print("square has four sides...")
# class circle(shape):
#     def show(self):
#         print("circle is round...")    
# OBJ = square()
# OBJ.show()
# # OBJ.design()
# obj = circle()
# obj.show()    
# # obj.design()

# Accessing in other child class
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def disp(self):
        pass
class square(shape):
    def disp(self):
        pass
class circle(shape):
    def show(self):
        print("circle is round...")  
    def disp(self):
        print("square has four sides...")  
obj = circle()
obj.show()  
obj.disp()  
