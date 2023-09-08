''' 
Simple Inheritance:
It has only one parent and one chlid class.
Syntx:
    class parent:
            properties
          
    class child(parent):
            properties
                +
            parent properties(can be accessed)
'''
class A:
    num1 = eval(input("enter a number: "))
    num2 = eval(input("enter a number: "))
    def add(self):
        print("Addition: ",self.num1+self.num2)
    def sub(self):
        print("Subtraction: ",self.num1-self.num2)
class B(A):
    def mul(self):
            print("Multiplication: ",self.num1*self.num2)
    def div(self):
        print("Division: ",self.num1/self.num2)
    def rem(self):
        print("Reminder: ",self.num1%self.num2) 
obj = B()
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.rem()       