''' 
Abstraction:
    It is a process of hiding the implementation details from the user.
    Only the highlighted set of services are provided to the user.
'''
def add():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    sum = a+b
    print("Addition: ",sum)

