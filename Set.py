'''
Set is data structure which is also called as collection of items in which we can 
represent a group of unique values as a single entity.
Syntax:
Set-name={item 1,item 2,.....,item n}       
Note:
1- We write items of set in curly braces{}
2- Insertion order is not preserved(like if we stored h at index 0 and f at index 1 on print they may return hf or fh)
3- Indexing and slicing not allowed 
4- Hetrogenious in nature(float,integer,boolian,string all types allowed to put in)
5- Mutable in nature(values can be added or deleted) 
'''
var= {}
print(type(var))
#It will print empty dictionary

#To have empty set 
var= set()
print(type(var))

#Insertion order is not preserved
var= {12,'Hussain',133.5,False}
print(type(var))
print(var)
'''
#Indexing and slicing not allowed
#Indexing
var= {12,'Hussain',133.5,False}
print(var)
print(var[1])
#Error as set object is not subscriptable
#Slicing
var= {12,'Hussain',133.5,False}
print(var)
print(var[1:2])
#Error as set object is not subscriptable
'''
#Hetrogenous in nature and ignore duplicates
var= {12,'Hussain',133.5,False,12,'Hussain'}
print(var)

#Mutable operations of set
'''
1-Add method 
This method takes one parameter as an input
'''
var= {12,'Hussain',133.5,False}
var.add(15.5)
print(var)
'''
2-Update method 
It is used to add more than one values  
It only allows string iteration  
It separates the string If [] are not used inside ()
[] these braces help update string as it is
'''
var= {12,'Hussain',133.5,False}
var.update("Jahangir")
print(var)

var= {12,'Hussain',133.5,False}
var.update("Jahangir",'Jhang')
print(var)

var= {12,'Hussain',133.5,False}
var.update(["Jahangir",'Jhang'])
print(var)

#Pop method: It takes no argument in set and pops value randomly in 2nd iteration but in one iteration it only removes the last value
var= {12,'Hussain',133.5,False}
print(var.pop())       #it will print the item that is poped only
print(var.pop())
print(var)

'''
Remove method: 
It can not be empty we have to pass an arugument
It gives us choice of what we want to remove but pop method removes randomly in set
'''
var= {12,'Hussain',133.5,False}
var.remove(133.5)
print(var)

#clear method:It clears all entries and returns empty set
var= {12,'Hussain',133.5,False}
var.clear()
print(var)

'''
Methamatical methods 
1- Union 
It prints all the unique values of both sets 
It can also be achieved by using or operator("|")
'''
var= {12,'Hussain',133.5,False}
var1={12,'Hussain',False,True,133.5,'Pakistan'}
print(var.union(var1))
print(var | var1)
'''
2-Intersection
It will print common values
It can also be achieved by using and operator("&")
'''
var= {12,'Hussain',133.5,55,'Jahangir'}
var1={12,'Hussain',False,True,133.5,'Pakistan'}
print(var.intersection(var1)) 
print(var & var1) 

'''
3-Differance method
It minuses the common values of 1st from 2nd set and write the rest values of 1st set
It can also be achieved by using and operator("-")
Symmetric differance 
This differance minuses common values from both and prints all the rest values from both sets 
''' 
var= {12,'Hussain',133.5,55,'Jahangir'}
var1={12,'Hussain',False,True,133.5,'Pakistan'}
print(var.difference(var1)) 
print(var - var1)
#Symmetric differance 
var= {12,'Hussain',133.5,55,'Jahangir'}
var1={12,'Hussain',False,True,133.5,'Pakistan'}
print(var.symmetric_difference(var1)) 