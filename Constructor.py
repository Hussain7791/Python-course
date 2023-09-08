''' 
Constructor:
    It is a special function that gets automatically called when object of class is created.
    The main purpose of constructor is to create and initialize the object.
    It is created only for any type of class.
    Constructor has the same name as the name of class.
Syntax:
    def __init__(self):       #Here init means initialization.
    #Here self is a referane parameter.Values cannot be initialized inside constructor without self parameter
    Defined varibale can also be only accessed by self parameter.Self points current object.
    #code
'''
# class A:
#     pass
# obj = A()             #here A() is a constructor
#We will have blank answer as we have not initialized any thing we made this class empty.
#But If I say that it has a default constructor self written and hidden by python then no one will believe.
#Lets make a same constructor by our own in a program.
class A:
    def __init__(self):
        pass
obj=A()
#So the output is same.It proves that this constructor was

#Why we need default constructor to manually create as it is ceated itself by python??
#We manually create default constructor so that we may add values in it or to code purposely.
#As python is not gonna write code for us in default constructor.
#We can perform task inside constructor.
 
# class A:
#     def __init__(self):
#         name = "Hussain"
#         print(name)
# obj=A()

# class A:
#     age = 23
#     def __init__(self):
#         name = "Hussain"
#         print(name," ",self.age) #here self points current object and age is a part of object so it can be called this way
# obj=A()

# class A:
#     def __init__(self):
#         print("Hassan")
#     def __init__(self):
#         print('Hussain')
# obj=A()
#This program show that if we initialize multiple default constructors in a program then only the value of last 
#will be printed on priority bases.

# Types:
#     1- Default constructor
#     2- Parameterized constructor

# 1- Default constructor:
#                 These are also  called empty constructors as they do not have any parameter.
# Note:
    #  If we dont define any constructor,the compiler automatically calls the default constructor.
# Syntax: 
    #    def __init__(self):        #Self is not a parameter but a referance argument 
    #        code
# e.g
# class A:
#     name = "Hussain"
#     def __init__(self):
#         print(self.name)
# obj = A()

# class A:
#     name = "Hussain"
#     age = 23
#     def __init__(self):           #Constructor function(calls itself)
#         address = "Jhang"          #address is local member of this constructor so it can only be accessed inside it
#         print(self.name," ",address)
#     def show(self):               #Normal function(to call normal function we have to call it through object manually)
#         print(self.age)
# obj = A()
# obj.show()
#self is only required to access the members of a class and it is not required to access local members of a constructor.

# 2- Parameterized constructor:
            #    It accepts arguments along with self 
# Syntax:
# class class_name:
#     def __init__(self,parameters):
#         code

# class A:
#     def __init__(self,name,age,address):
#         print(name,age,address)
# obj = A('Hussain',23,'Jhang')
# If we do not add argument against parameter address it will show error as
# class A:
#     def __init__(self,name,age,address):
#         print(name,age,address)
# obj = A('Hussain',23,None)
# The situation can be handeled by using None with captital N.
# class A:
#     def __init__(self,name,age,address):
#         print(name,age,address)
# obj = A('Hussain',23,None)
#We can also change the value of argument inside the constructor as:
# class A:
#     def __init__(self,name,age,address):
#         address = "Jhang"
#         print(name,age,address)
# obj = A('Hussain',23,None)
#Now if we want to call class member variables we will use self function.
class A:
    father_name = "Jahangir"
    def __init__(self,name,age,address):
        address = "Jhang"
        print(name,age,address,self.father_name)
    def show(self):
        print(self.father_name)
obj = A('Hussain',23,None)
obj.show()
#HERE SHOW IS A NORMAL FUNCTION WHILE WE HAVE A CONSTRUCTOR AS WELL.THAT CALLS ITSELF.        










