'''
Flow control:
It is basically the order in which statements will be executed at run time
1-Conditonal statement(if,if else,else if)
if: for single condition statment execution
if else: for single condtion to execute two statements
else if: If we have many conditions 
Syntax:
if condition:
    statement            #the space that is created after if condition is called python identation

if condition:
    statement
else:
    statement   
    
if condition:
    statement
elif condition:
    statement  
else:
    statement    
'''
#If 
user_input= eval(input("enter a number : "))
if user_input %2 ==0:
    print('Number is even')

#If else
user_input= eval(input("enter a number : "))
if user_input %2 ==0:
    print('Number is even')
else:
    print('Number is odd')
 
#else if   
age= eval(input("enter your age : "))
if age < 18:
    print('You are too young to marry')
elif age>60:                              #for multiple conditions
    print('You are too old for marriage')    
else:
    print('We will try to find a perfect match for you')    
    