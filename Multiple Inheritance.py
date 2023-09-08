''' 
Multiple Inheritance:
It has multiple parent classes and one child class.
Syntax:
    class parent1:
              properties
    class parent2:
          .  properties
          .
          .
          .
          .
          .
    class parentN:
          properties
    class chlid(parent1,parent2,......,parentN)
          properties
'''
class Hussain:
    back = "Oracle database & Java"
    def Backend(self):
        print("Backend task implemented using: ",self.back) 
class Hassan:
    front = "HTML CSS & Javascript"
    def Frontend(self):
        print("Frontend task implemented using: ",self.front) 
class Teamlead(Hussain,Hassan):
    def show(self):
        print("dynamic website created.....")
obj = Teamlead()
obj.Backend()
obj.Frontend()
obj.show() 
    

        
    

















