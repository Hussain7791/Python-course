import Modules
Modules.show()
Modules.disp()
print('Jhang')

#if you dont want to write module name again and again you can use this method 
from Modules import disp,show
disp()
show()

#If we dont want to write the individual name of values of the module we want 
#to import then we will use * sign which means(all)
from Modules import *
disp()
show()

#To change the name of function used in the imported module we will use (as) function
from Modules import disp as burp
burp()

from Modules import disp
from testmodule import disp as bang        #here we have name conflicting so we will use as function
disp()                 
bang()