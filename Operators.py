'''Operators:
   They are symbols that perform certain tasks.
   Various sets of operators in Python:
   1-Arethmatic operators(-, +, *, /,  //, **)
   2-Relational operators(<, >, <=, >=, ==, !=)
   3-Logical operators(and, or, not)
   
   4-Bitwise operator(Only applicable on int and boolean values)
   & -> bitwise and
   | -> bitwise or
   ^ -> bitwise XOR
   ~ -> bitwise complement
   >> -> bitwise shift right
   << -> bitwise shift left
   
   5-Assignment operator(=)
   
   6-Special operator
   a-Identity operator(is,is not)
   b-Membership operator(in,not in)
   ''' 
#Arethmatic operators(-, +, *, //, **)   
a=9
b=2
print(a+b)   
print(a-b)     
print(a*b)     
print(a/b)     
print(a//b)     #This is a type of floor division or integer division that rounds the fractional value
print(a**b)     #This operator is used to create power of values**
   
#Relational operators(<, >, <=, >=, ==, !=)   
a=9
b=2
print(a<b)   
print(a>b)     
print(a<=b)     
print(a>=b)     
print(a==b)     
print(a!=b)    
   
#Logical operators(and, Or, not)   
a=9
b=2
print(a<b and a>b)      #It will only be true when both conditions are true
print(a<b or a>b)       #It will be true when any of the two conditions is true.
print(not(a<b and a>b)) #It will change the true condition into false and vise versa.
print(not(a<b or a>b)) 

'''
Bitwise operator(Only applicable on int and boolean values):

& -> bitwise and(If both 1 then 1 else 0):
This operator works by converting the digits into their binary form and 
then after finding answer by applying logics gives our answer back in normal form.
i.e digit   binary
     5   ->   101
     6   ->   110 
              100(4)    
'''
print(5 & 6)

'''
| -> bitwise or(If any 1 then 1 else 0)
i.e digit   binary
     5   ->   101
     6   ->   110 
              111(7) 
'''
print(5|6)

'''
^ -> bitwise XOR(if both same then 0 else 1)
i.e digit   binary
     5   ->   101
     6   ->   110 
              011(3)
'''
print(5^6)

'''
~ -> bitwise complement(give value into -ve and then add -1(m=-n-1))
m=-n-1
m=-5-1
m=-6
'''
print(~5)

'''
>> -> bitwise shift right
It will shift the value to the right side
e.g If we have a binary of 4 one's as 1111. It means these are 
stored in four box spaces of the memory location.When we use our 
right shift bitwise then the value of all boxes will be shifted to 
right making space free in the 1st box and kicking one 1 out of the space 
leaving behind three one's 111.
i.e digit   binary
     15   ->  1111
     15   >>   111(7)
'''
print(15>>1)   #It means we are shifting 15 to right one time

'''
<< -> bitwise shift left
When we will move on the left side it will create a new box in left and will move all
values to the left leaving the last right most box as 0.
i.e digit   binary
     15   ->  1111
     15   << 11110(30)
'''
print(15<<1)     #It means we are shifting 15 to left one time

#Assignment operator(=)(It is used for assigning value to variables)
a=55
print(a)

'''
Special operator: 

a-Identity operator
It tells if the id of two values are same 
is 
is not
'''   
a=5
b=5
print(a is b)
print(id(a))
print(id(b))
#Hence both ids are same

a=5
b=6
print(a is not b)
print(id(a))
print(id(b))
#Hence both ids are not same

'''
b-Membership operator
It tell if the data is present in our variable or not
in 
not in
'''
var="Pakistan is a great country"
print("great" in var)
print('Pakistan' not in var)