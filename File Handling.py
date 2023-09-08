'''
File Handling:
File:
File is the name of memory location on disk that stores data permanantly.
Why we need files:
Files store data permanantly but variable is short time memory location its data is deleted after execution
File Handling:
This is a mechanism by which we can handle(read,write,create,append....etc)the file.
Syntax:
file-obj = open('file-path', 'mode')   #file-path means location of file and mode means operation(read,write,create,append....etc) to be done
open: It is a function of python to work with files and it takes two parameters
file-obj: File is stored in a file object 
file-path: Copy the location of file folder where you want to perform operations and paste in file path parameter

File modes:
x = empty
r = read
w = write
a = append
r+ = both read and write
b = binary mode

File operations:
1-Create
2-Read
3-Write
4-Copy
5-Delete 
6-Close etc...
'''
#open("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt","x")         #After pasting path change single slash into double slash
#\A.txt This means we are creating a text file named A
#As our file is empty there is no content in it so we set mode as x which means empty
#This whole file is now to be stored in an object we can say f.

#Empty file:
# f=open("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt","x") 
# print('File has been created sucessfully......')     #This is Just to tell the user that file is created and ready to be checked

#Write Operation:
# f=open("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt","w") 
# f.write('Learn Python\n Hussain | Jahangir' )
# print('Data has been written sucessfully......')
  
# Read operation:
# f=open("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt","r") 
# print(f.read(32))   #30 words to be read and printed in console # We enter size(number of words to be read) in braces of read function
# print( 'Data has been readed sucessfully......')
# Read operation always takes some value in numbers and prints the data from the file equal to that number
# It also consider spaces as a word.

# Readline function:
# It only reads a single line data and we dont need to enter the words or numbers to read our data.
# f=open("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt","r") 
# print(f.readline())

# Readlines function:
# If you want to read all data in your created file then you will use readlines function.It will print data in the form of list.
# f=open("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt","r") 
# print(f.readlines())

#Changing file name not found in folder:
# f=open("C:\\Users\\Hussain\\Desktop\\Python full course\B.txt","r") 
# We have changed the name of file A as B which is not found in folder. We will have a runtime error that file is not found
# print(f.readlines())

# Exception handling for the file:
# try:
#     f=open("C:\\Users\\Hussain\\Desktop\\Python full course\B.txt","r") 
#     print(f.readlines())
# except:
#     print('File not found....Please create one 1st!')

# Close Operation:
# try:
#     f=open("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt","r") 
#     print(f.readlines())
# except:
#     print('File not found....Please create one 1st!')
# else:
#     f.close()                   #Used to close the opened file automatically
#     print("File closed....!")

# Copying Data into another file:
# For data to be copied in another file we have to write the code in with and as functions 1st file will be inside try and 
# 2nd will be inside 1st file then we will apply for loop to copy data of 1st file in 2nd then will repeat the same process
# of except and else.
# try:
#     with open("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt","r") as f2:
#         with open("C:\\Users\\Hussain\\Desktop\\Python full course\B.txt","w") as f3:
#             for i in f2:
#                 f3.write(i)
# except:
#      print('File not found....Please create one 1st!')
# else:
#     f2.close()                   #Used to close the opened file automatically
#     print("File closed....!")

# Deleting a file:
# We will use operating system module to delete a file as the data is stored on the disk
# The os module will be imported from the built-in libraries of python. 
# 1st we will write a if statement to see if path exists in os by printing location in braces 
# os.remove will be used to remove the file same location will be given in the braces of remove funtion
# Print a message for the convinence of user that the file is deleted 
# In else print file not found which will be executed when file is not found asked to be deleted
import os
if os.path.exists("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt"):      #We will add the location of file to be deleted here
   os.remove("C:\\Users\\Hussain\\Desktop\\Python full course\A.txt")
   print('File deleted sucessfully....!')
else:
    print("File not found....!")












