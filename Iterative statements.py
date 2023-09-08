'''
Iterative statements(for loop,while loop)
Syntax:
for var-name in range(start,end):
    statement
    
while loop     #we use while loop when we are unaware of starting and ending points 
while condition:
    statement
'''
#for loop
user_input = eval(input("enter a number : "))
for number in range(1,11):    #It will print a loop from 1 to 10 cz it prints 1 less then ending 
    print(user_input*number)   
 
#While loop    
password = "Hussain"
input_password = input("enter password : ")
while password != input_password: #Ask password from user till password becomes equal to input_password
    input_password= input('enter password : ')
else:
    print('Unlocked!! ')

    