'''
Function:
It is a group of statements that are executed only when we call a key we name function.
Why we use function....??
1- To increase code reuseability
2- Function returns value as a result 
3- we can pass values to the function called parameters and the function is called parameterized function.
Types:
Pre-defined:
Develeped by python developer(built in)
len()
print()
int()
etc.

User-defined:
We develop these functions for the sake of our convinence
Hussain()
Jhang()
Add()
etc.
Syntax:
We use def when we write function as def is short form of (define)
def function_name:
    statement
'''
'''
#Pre-defined:
print('I am a beginner in python programming')
print(len('I am hussain'))
'''
#user-defined:
'''
a = 8
b = 4
print('add : ',a+b)
print('mul : ',a*b)
print('sub : ',a-b)
print('div : ',a/b)
#To avoid repeateetion of code we use functions
#Function will recieve parameters as an input 
#It will also returns some value as an output
'''
'''
#Converting the values of code into function to reuse it
a = 8
b = 4
def calculator(a,b):
    print('add : ',a+b)
    print('mul : ',a*b)
    print('sub : ',a-b)
    print('div : ',a/b)
calculator(8,4)             #This is the way we call the function.Without function call function will not work
calculator(14,7)
calculator(16,4)
calculator(50,25)


def greet():
    #print('Good evening')    
#greet()
    return "Good evening"
print(greet())

#here we are calling function and asking our interpreter to print greet fun as well so after function call we will have 
#a value none. This is because we have not returned any value. By returning value we can also write and save the value of fun in another var.
   
def greet():
    print("Good evening")
msg = greet
print(msg)

def greet(name):
    print("Good evening",name)
greet('Hussain')

Type of arguments:
1- Positional argument
a-order should be maintained
b-Seqenece of input will define the sequence of received data     
c-no. of parameters = no. of arguments
e.g
'''
'''
def greet(firstname,lastname):       #Here passed vales are parameters 
    print("Good evening",firstname,lastname)
greet('Hussain','jahangir')          #these values are arguments
'''
'''
2- Keyword arguments:
a- Order is not important
b- no. of parameters = no. of arguments     
c-Keyword argument should follow positional argument
'''
'''
def greet(firstname,lastname):       #Here passed vales are parameters 
    print("Good evening",firstname,lastname)
greet(lastname='Jahangir',firstname='Hussain')          #these values are arguments
'''
'''
3- Default argument:
a- Order is important
b- no. of parameters may or may not be equal to no. of arguments
'''

''' def greet(name='guest'):         #Now this is what we set guest as a default value
    print("Good evening",name)   #It means if we will change the value in our argument then value will change accordingly else we will  
greet()                          #have the same default value.

#Changing value in argument:
def greet(name='guest'):         
    print("Good evening",name)    
greet('Hussain') 
'''

#Variable lenght arguments:
#Passing no data
def test(*args):         
    print(args)
    print(len(args))
    print(type(args))
test()    

#Simple arguments:
def test(*args):         # '*' is used for simple argument when we dont know the exact values to be passed. 
    print(args)
    print(len(args))
    print(type(args))     # This is a tuple type 
test('Pakistan',34,'Saudi Arabia',12.5)  # We can pass multiple values here or may not pass any value 

#Keyword arguments:
def test(**kwargs):      # '**' Is used to pass keyword arguments
    print(kwargs)
    print(len(kwargs))    
    print(type(kwargs))  #This is dictionary type
test(country='Pakistan',firstname="Hussain")  #We have to pass values and keys as well



