''' 
Multi-level Inheritance:
        It has one parent class and multiple child classes.
Syntax:
    class parent:
              properties
          
    class child1(parent):
          properties
              +
          parent properties(can be accessed)
    class child2(child1):
          properties
              +
          child1 properties(can be accessed)
'''
class Father:
    surname = "Sayyad"
class son(Father):
    def show(self):
        print("Ali",self.surname)
class grandson(son):
    def disp(self):
        print("Hussain",self.surname)
obj1 = grandson()
obj1.show()
obj1.disp()
