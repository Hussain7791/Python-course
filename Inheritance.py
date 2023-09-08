''' 
Inheritance:
       Inheriting all the properties of class in another class is called inheritance
syntax:
      class parent:
          properties
          
      class child(parent):
          properties
              +
          parent properties(can be accessed)      
'''
# class parent:
#     a = 10
#     _b = 20
#     c = a+_b
#     print(c)
# class child(parent):
#     d = 70
#     h = 80
#     f = h-d
# obj = child()
# obj.f
# obj.c

# class parent:
#     def lands(self):
#         print("100 Achres of lands is owned by parents")
# class child(parent):
#     def money(self):
#         print("Having 1 cror in child's account")
# obj = child()
# obj.lands()
# obj.money()
# Hence we can see that the child class can inherit the properties of parent.
# But parent cannot access the properties of child as in parent class child class is not inherited 
class parent:
    def lands(self):
        print("100 Achres of lands is owned by parents")
class child(parent):
    def money(self):
        print("Having 1 cror in child's account")
obj = parent()
obj.lands()
obj.money()
# It will onlyy print the properties of parent class and will show error for the child class accessing

''' 
Types:
1- Simple Inheritance(1 base and derived class)
2- Multiple Inheritance
3- Multi-level Inheritance
4- Hierarchical Inheritance
5- Hybrid Inheritance
'''
  