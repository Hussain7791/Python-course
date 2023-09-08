'''
List:
    It is a data structure which is also called as collection of items in which we can store 
    anything like string,float,integer
    syntax:
    list name=[item 1,item 2,....,item n] 
    
    Note:
    1-We write the items of list in square brackets[] and each item is seprated by comma(,).
    2-Duplicates are allowed
    3-Mutable(value can be updated) in nature
    
    Live practical:
    1-Create empty list
    2-List with some values
    3-Indexing
    4-Slicing
    5-Count list items
    6-Append 
    7-Pop
    8-Insert
    9-Extend
    10-Sort
    11-Reverse
    12-Nested list
    13-List comprehension
    14-Copy
    15-Lenght of list
'''
#Create empty list
list1=[]
print(type(list1))

#List with some values
list2=[10,'Hussain',13.5,True,10,'Jahangir']
print(list2)
print(type(list2))

#list function
list3=list()
print(type(list3))

#Indexing:Each stored value start from 0 index.We can drive value by Just giving index number this is indexing
list4=[10,'Hussain',13.5,True,10,'Jahangir']
print(list4[3])
'''
Slicing: In slicing we have to select the starting value and a one more than the ending value(end-1)to get
desired result
'''
list5=[10,'Hussain',13.5,True,10,'Jahangir']
print(list5[1:4])

#Methods of list:
#Count list Items:
list6=[10,'Hussain',13.5,True,10,'Jahangir']
print(list6.count(10))

#index finding:
list7=[10,'Hussain',13.5,True,10,'Jahangir']
print(list7.index(True))
#for same values
list7=[10,'Hussain',13.5,True,10,'Jahangir']
print(list7.index(10))
#Here(10,1)tells the interpreter to skip 0 index and start finding 10 from 1 index
list7=[10,'Hussain',13.5,True,10,'Jahangir']
print(list7.index(10,1))

#Insert
list8=[10,'Hussain',13.5,True,10,'Jahangir']
list8.insert(3,'Python is best')   #We have inserted a string at location 3.
print(list8)

#Pop(deletion)
list8=[10,'Hussain',13.5,'Python is best',True,10,'Jahangir']
list8.pop(3)   #We have deleted a string at location 3.
print(list8)
#Note:If we donot give any index to pop then it automatically deletes last element

#Extend
list9=[10,'Hussain',13.5,True,10,'Jahangir']
list10=['Python is awesome',95]
list9.extend(list10)
print(list9)

#Copy
list9=[10,'Hussain',13.5,True,10,'Jahangir']
list11=list9.copy()
print(list11)
#Another way
list9=[10,'Hussain',13.5,True,10,'Jahangir']
list11=list9[:]  #We have 0 on lest side of colon(:) and n-1 on right side by default.So it copies whole list
print(list11)

#Sorting
#We need same type of values for sorting
list12=[10,1,5,8,55,2]
list12.sort()
print(list12) #By default assending order sorting
#Decending order short
list12=[10,1,5,8,55,2]
list12.sort(reverse=True)
print(list12) 

#Reversing 
list12=[10,1,5,8,55,2]
list12.reverse()
print(list12) 

#Nested list: Creating a list inside a list
list13=[10,'Hussain',13.5,True,10,['Jahangir',['python']]]
print(list13)

#List comprehension
list13=['Hussain','Jahangir','Noman','Ali','Faizan']
a=[word for word in list13 if word.endswith('n')]  #It means for each word in list13 if word ends with n then consider it as a word
print(a)
#Or
list13=['Hussain','Jahangir','Noman','Ali','Faizan']
a=[word for word in list13 if word.startswith('H')]  #It means for each word in list13 if word starts with H then consider it as a word
print(a)

#List Unpacking
list14=['Hussain','Jahangir']
h1,h2=list14
print(h1)
print(h2)

#Appending: It takes exactally one argument to add at last.
list14=['Hussain','Jahangir']
list14.append(19)
print(list14)

#Length of list
list15=[10,'Hussain',13.5,True,10,'Jahangir']
print(len(list15))        #This will tell us the length of list starting from 1 to n.