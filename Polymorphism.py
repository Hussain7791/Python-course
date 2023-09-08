''' 
Polymorphism:
    It means ability to take various forms.
    Same object having different behaviour. 
'''
# print(5+5)   #Simple addition
# print("5"+"5")    #Conctination
# Same values with different behaviours
# print(len("Hussain"))
# print(len(["Hussain","Hassan"]))     #list
# len function is same but it showing different behaviours in both conditions  
''' 
Ways to perform polymorphism:
1-Method Overloading
2-Method Overriding
'''

''' 
Method Overloading:
    Whenever class contains more than one methods with same name and different parameters this is called Overloading. 
'''
# Same class with different functions

# class A:
#     def show(self):
#         print("welcome...")
#     def show(self,firstname=''):
#         print("Welcome ",firstname)
#     def show(self,firstname='',lastname=''):
#         print("Welcome ",firstname,lastname)
# obj = A()
# obj.show()
# obj.show("Hussain")
# obj.show("Hussain","Jahangir")

# Same function called many times with different parameters
# class A:
#     def show(self,firstname='',lastname=''):
#         print("Welcome ",firstname,lastname)
# obj = A()
# obj.show()
# obj.show("Hussain")
# obj.show("Hussain","Jahangir")


''' 
Method Overriding:
    Whenever a program contains more than one functions with same name and same types of parameters in parent and child classes 
    then the it is called overriding.
    Method name is written with the same signature.
    Without Inheritance we can not perform overriding
'''
# class A:
#     def disp(self):
#         print("This is parent class method")
# class B(A):
#     def disp(self):
#         print("This is child class method")
# obj = B()
# obj.disp()         #Here B class function overrides function of A class     

# To Access parent class values in this case we will use a builtin function super as 
class A:
    def disp(self):
        print("This is parent class method")
class B(A):
    def disp(self):
        super().disp() 
        print("This is child class method")
obj = B()
obj.disp()  
# Hence in this way we can solve the overriding problem.













