''' 
Exception:
It is nothing but runtime errors and it occurs due to incorrect implimentation of logic
e.g If we are trying to transfer money to another account without having balance in our own account then  
we will be notified insufficient funds. This is a case of exception.
e.g
a=10
b=0
c=a/b;
print(c)     #As no value is divisible by zero we will have an error,Code will stop executing here 
print('Hussain')  #This value will not print even due to error in code before 
Exception Handling:
It is a method of handling runtime errors
Blocks of handling exception:
1- try       # We will write risky code(with more chances of exception) in try block only
2- except    #This block will only execute when we have error or exception in try block
3- else      #This is optional it can or cannot be used. If there is no exception in try block then else will run and vice versa
e.g
a=10
b=0
try:
   c=a/b
   print(c)
except:
    print('Handled')
'''    
# a = eval(input('enter a no: '))
# b = eval(input('enter a no: '))
# try: 
#    c= a/b
#    print('Result: ',c)
# except:
#     print('No number can  be divided by 0')
# print('Hussain...')
 
# With else block:
a = eval(input('enter a no: '))
b = eval(input('enter a no: '))
try: 
   c= a/b
   print('Result: ',c)
except:
    print('No number can  be divided by 0')
else:
    print('Hussain...')        #It will only run when try block has no exception and runs smoothly













