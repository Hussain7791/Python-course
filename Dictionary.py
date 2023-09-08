'''
Dictionary
It is a data structure in which we represent group of objects as a key value pairs
Syntax:
dict-name= {key:values}
Note:
1- Indexing nad slicing not allowed 
2- Insertion order is preserved(index number of keys and values will remain fixed)
3- Hetrogenious in nature(float,integer,boolian,string all types allowed to put in)
4- Mutable in nature
5- Key must be unique but duplications in values is allowed
'''
#Empty dictionary 
var={}
print(type(var)) 
#e.g
var={'Name':'Hussain'}
print(type(var))
print(var) 
#same values
var={'Name':'Hussain', 'age': 23 , 'username': 'Hussain'}
print(type(var))
print(var)
 
#same keys: It will ignore the last value and prints the new value
var={'Name':'Hussain', 'age': 23 , 'Name': 'Jahangir'}
print(type(var))
print(var)

#Excessing value directly from the key
var={'Name':'Hussain', 'age': 23 , 'Name': 'Jahangir'}
print(type(var))
print(var)
print(var['age'])
print(var['Name']) #As we took same keys so it will ignore 1st and jumps to the 2nd.

#pop method
var={'Name':'Hussain', 'age': 23 , 'Name': 'Jahangir'}
print(var.pop('Name'))  #It also returns the updated value only
print(var)
#or
var={'Name':'Hussain', 'age': 23 , 'Name': 'Jahangir'}
var.pop('Name')
print(var)

#Excessing value through Get method
var={'Name':'Hussain', 'age': 23 , 'Username': 'Jahangir','Password': 79549822}
print(var.get('Password'))
#For a random key that is not in dictionary we can give a message for user understanding
var={'Name':'Hussain', 'age': 23 , 'Username': 'Jahangir','Password': 79549822}
print(var.get('Helpline','Not available')) #if key not found message will print else it will be ignored
print(var.get('Helpline'))      #Without meassage it will print none 
print(var.get('Password'))

#clear method:
var={'Name':'Hussain', 'age': 23 , 'Username': 'Jahangir','Password': 79549822}
var.clear()
print(var)
#It will give us an empty dictionary

#keys and values method
var={'Name':'Hussain', 'age': 23 , 'Username': 'Jahangir','Password': 79549822}
print(var.keys()) 
print(var.values()) 
#We can drain dictionary keys and values by using this method
#We can also print items as
print(var.items())

#Printing Items using loops
var={'Name':'Hussain', 'Age': 23 , 'Username': 'Jahangir','Password': 79549822}
for key, values in var.items():
    print(key,values,sep=" - ")             #using separater to take manual separating results

#Changing the value of Key
var={'Name':'Hussain', 'Age': 23 , 'Username': 'Jahangir','Password': 79549822}
var['Age']=31
print(var)


 