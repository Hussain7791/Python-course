''' 
Access modifiers:
They are used to set the limit of member accessability.
These are used to secure or restrict the data.
Public:
They are simply represented as var(for variable).This portion can be accessed in same class, derived class, same package and other class as well.
Protected:
Varible in this portion is represented by single underscore before the variable name as _var. 
This portion can be accessed in same class, derived class and same package 
Private:
Varible in this portion is represented by double underscore before the variable name as __var. 
This portion can be accessed in same class only.
Note:
In same package we can create a lot of classes
'''
# class A:         #Parent class
#     a = 10       #Public member
#     _b = 20      #Protected member 
#     __c = None     #private
#     print(a," ",_b," ",__c)
# This is a simple program to show that we can access all types of modifiers in same class.
#     def add(self):
#         self.__c=self.a+self._b
#         print("Addition: ",self.__c)  
# obj = A()
# obj.add()
# As we are in the same class so we are able to use all modifiers.Lets try to access them outside  the class.
# print(obj.a)  
# print(obj._b) 
# print(obj.__c) 
# As __c is private so it cannnot be accessed outside the class as creates error. rets of all can be accessed easily.
# class B(A):     #Child class
#     def show(self):
#         print(self.a)
#         print(self._b) 
#         print(self.__c) 
# obj = B()
# obj.show()
# Hence we see that in inheritance we can acsess both public and protected members of class in derived class but private is only accessible inside same class  

# Accessing through object in inherited class 
# class A:        
#     a = 10       
#     _b = 20        
#     __c = None     
#     print(a," ",_b," ",__c)
# class B(A):
#     pass    
# obj = B()
# print(obj.a)
# print(obj._b) 
# print(obj.__c)     #this can not be accessed here as it is totally secure.

#Accessing modifiers in other class of same package 
class A:        
    a = 10       
    _b = 20        
    __c = None     
    print(a," ",_b," ",__c)
class B(A):     
    def show(self):
        print(A.a)        #Accessing by the name of class to be accessed 
        print(A._b) 
        print(A.__c) 
obj = B()
obj.show()









