'''
Modules:
These are group of functions,variables and classes that are saved to a file.
NOTE:
Code Reuseability:
It is used to reuse the code of a project in another project
import keyword is used with the module name to transfer the code from that module to new one. 
It saves our time and we can use code again as well 
If we have a module python.py then in 2nd module we have to use only the module name python only.
Types:
1- Pre-defined:(random, calender, keyword)
These are already defined modules by developer we just import the codes in our modules
2- User-defined:(first, Hussain, Jahangir)
These are defined by the user or us as a developer and we use our own modules to import in other modules
example:
old project                     new project
Modules.py                      List.py
def show():                     import Modules
print('hello')                  Modules.show()
'''
#pre-defined modules:
import calendar
print(calendar.month(2023,8)) 

import keyword
print(keyword.kwlist)

#user-defined modules:
def show():
    print('Hi Hussain')
show()
def disp():
    print('Hi Hassan')
disp()
'''
Module aliasing:(changing the name of function after import in next module)
--------------------------------------------------------------------------
1-To improve readability
2-To prevent name conflicting(As if we have same name of functions in two differnt modules being imported we will use it)
'''

