''' 
Hierarchical Inheritance:
It has one parent class and multiple child classes.But each child class can access parent properties separatly.
Syntax:
    class parent:
              properties
          
    class child1(parent):
          properties
              +
          parent properties(can be accessed)
    class child2(parent):
          properties
              +
          parent properties(can be accessed) 
'''
class Father:
    surname = "Jahangir"
    def show(self):
        print("My name is ",self.surname)
class son1(Father):
    def disp(self):
        print("My name is Hussain",self.surname)
class son2(Father):
    def disp1(self):
        print("My name is Hassan",self.surname)   
s1=son1()
s2=son2()
s1.show()
s1.disp()
s2.show()
s2.disp1()













     