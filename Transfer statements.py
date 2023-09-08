'''
Flow control:
Transfer statement(Break,continue,pass)
It is used to transfer or stop the control of the program 
Break:
When control of a program recieves break statement it stops the program at the spot
Continue:
It will skip a statement if true for a while 
Pass:
It will bypass the statement  


#pass
if "a" in "Hussain":
    pass                   #this is used if we don't want to write the body at the time
'''
#Continue
for num in range(1,11):
    if num % 2 == 0:
        continue            #as in condition continue statement will skip all even numbers
    else:
        print(num)
        
#Break
for num in range(1,11):
    if num % 2 == 0:
        break          #It will only print 1 as on 2 the condition becomes true and break will end program
    else:
        print(num)        
        