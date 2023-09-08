'''
Class:
Class is a blueprint for an object.Real-world entities have some properties or behaviours 
which is represented by class variables and methods in programming.
Syntax:
class class-name:
    variables
    methods
#Class is just a template it has no memory location untill or unless we create object for it.

Object:
As we know class is a logical entity while an object is a physical or real entity that works on class data.
Note:
Each object has a distinct role 
Object create space on memory as per class members
Syntax:
obj-name = class-name()
'''
# class A:
    
# obj= A() 

# We can not keep class empty like this we will have IndentationError otherwise.

# To make an empty class we will use pass keyword in class body.
# class A:
#     pass    #It will pass the program so that we may write code later or keep it empty
# obj=A()    #object is only needed to access the members of class

# class A:
#     age=10
#     print("age = ",age) 
# obj = A()
 
#Default constructor:
''' Python adds a Default constructor in class itself hidden from us.
If we will add it ourselves then we can print the same code in class 
multiple times just by creating more and more objects
'''
#e.g:
# class A:
#     def __init__(self):       #This is a default constructor.
# Self is a referance parameter that refers current object      
#       age=10
#       print("age = ",age) 
# obj = A() 
# obj1 = A()
# obj2 = A()

# class A:
#     age=10
#     print("age = ",age) 
# obj = A()               #These are three ways of accessing class values in python
# print(A.age)
# print(obj.age)         
#Now as our string "Learn Python" is not saved in any variable to access this string it should be 1st line of code
#It can be accessed by using document attribute of  
# class A:
#     "Learn Python"
#     age=10
#     print("age = ",age) 
# obj = A()               #These are three ways of accessing class values in python
# print(A.age)
# print(obj.age) 
# print(obj.__doc__)       #Accessed by object 
# print(A.__doc__)         #Accessed by class name
 
# function in class:
# class A:
#     age=10
#     def fun(self):   #self parameter is compulsory here as it points object without this parameter we will have a error.
#         name = "learn coding"
#         print(name)
# obj = A()
# obj.fun()               
# print(A.age)
# print(obj.age) 

#To print document which is inside a function:
# class A:
#     age=10
#     def fun(self):
#         "Hussain Jahangir"   
#         name = "learn coding"
#         print(name)
# obj = A()
# obj.fun()
# print(obj.fun.__doc__)               
# print(A.age)
# print(obj.age)

# Parameterized function:
# class A:
#     def fun(self,age,name,adress):
#         print(age," ",name," ",adress)
# obj = A()
# obj.fun(10,"Hussain","Jhang")

# Lets do the same process with constructor.Constructor calls itself.
class A:
    def __init__(self,age,name,adress):
        print(age," ",name," ",adress)
obj = A(10,"Hussain","Jhang")
obj1 = A(20,'Hassan',"Jhang")
#By this method we can have differnt values just by creating objects.