'''
Tuple is a data structure which is also called collection of items in which we can store anything like
float,integer,string.
Syntax:
tuple-name=(item 1,item 2,.....,item n)
Note:
1-We write the items of tuple in parenthisis() and each item is seprated by comma(,).
2-Duplicate values are allowed 
3-Immutable(cannot perform changes(nothing can be added or deleted)) in nature
''' 
var=(1,'Hussain',True,10.5)
print(var)
#If we store more than one values in a varible without putting them in brackets in this case it will still be considered as tuple.
#Or simply adding comma after single value will be considered as tuple.e.g

#1
var= 1,'Hussain',True,10.5
print(type(var))
print(len(var))

#2
var= 1,
print(type(var))

#3
var= 1
print(type(var))

#copying
var= 1,'Hussain',True,10.5
var1=var
print(var1)

#Indexing
var= 1,'Hussain',True,10.5
print(var[2])
#a
var= (1,'Hussain',True,10.5)
Op=var.index(10.5)
print(Op)

#Unchangeability
var= 1,'Hussain',True,10.5
var[1]='jahangir'
print(var)
#OR
var= (1,'Hussain',True,10.5)
Op=var.pop()
print(Op)
#It will cause error as tuple doesn't support items assignment 