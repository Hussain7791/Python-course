''' 
Encapsulation:
       Python provides access to all the variables and methods globally.
       By using encapsulation we can restrict the variables and methods global access by
       making them private or protected  
Note:
   single underscore(protected)
   double underscore(private)
'''
class A:
    _a =10
    __b=20
    def show(self):
        print("a= ",self._a)
        print("b= ",self.__b)
obj = A()

obj.show()
print("outside of class",obj._a)    #call by object
#print("outside of class",obj.__b)
print("outside of class",A._a)     #call through class name