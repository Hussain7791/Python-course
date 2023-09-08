'''   
Multithreading:
    It is technique which allows the CPU to execute multiple threads(small tasks) of on process 
    at the same time.
    The purpose of multithreding is to run multiple tasks and functions at the same time 
    Example:
    Single threading:
    We make a program in python with two functions the program is by default a main thread 
    when we call both functions one function execute 1st and the other waits for some seconds 
    and executes after the 1st function's execution. 
    Multithreading:
    In this type we have same situation of a program having two functions(fun1&fun2) but this 
    time we have made two threads(t1 & t2) inside main thread. main thred is to execute the 
    program only but we will allot each function to each thread(t1 & t2) By doing this functions
    will execute at the same time as both threads perform their work at a time.    
Thread:
It is a pre-defined class in python which is available in threading module.
Thread is a basic or small unit of CPU and it is well known for independent execution 
Thread class methods:
1- Run()  It is the entry point of any thread all code is written inside it
2- start() This us used to call the run() method
3- Join()  If many threads are working simultaneously but we want that a thread runs in a particular time and then next come and executes in same time then we use join()
4- is-alive() It tells us if the thread is in running state or dead state 
5- SetName() We can set the name of thread by it
6- Getname() It gets the name of thread  
'''
# Single threading:
# class A:
#     def run(self):
#         for i in range(5):
#             print("Hussain")
            
# class B:           
#     def run(self):
#         for i in range(5):
#             print("Hassan")
# t1 = A()
# t2 = B()
# t1.run()
# t2.run()

# As our system is fast so we cant judge the time differance so we will import time for better understanding.

# from time import sleep
# class A:
#     def run(self):
#         for i in range(5):
#             print("Hussain")
#             sleep(1)
# class B:           
#     def run(self):
#         for i in range(5):
#             print("Hassan")
#             sleep(1)
# t1 = A()
# t2 = B()
# t1.run()
# t2.run()

# Multiple Threading

# from threading import Thread
# from time import sleep
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hussain")
#             sleep(1)
# class B(Thread):           
#     def run(self):
#         for i in range(5):
#             print("Hassan")
#             sleep(1)
# t1 = A()
# t2 = B()
# t1.start()
# t2.start()
# print("Jhang")

# We will use join to ask main thread print this last call print("Jhang") in the last and not to disturb the multi threads function as: 

# from threading import Thread
# from time import sleep
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hussain")
#             # sleep(1)
# class B(Thread):           
#     def run(self):
#         for i in range(5):
#             print("Hassan")
#             # sleep(1)
# t1 = A()
# t2 = B()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Jhang")


# Get name And Set Name in multithreading:

# from threading import Thread , current_thread
# def disp():
#     print("Default Child thread name: ",current_thread().getName())
#     current_thread().setName("Hacker")
#     print("New Child thread name: ",current_thread().getName())
    
# t1 = Thread(target=disp)
# t2 = Thread(target=disp)
# t1.start()
# t2.start()

# print("Default Main thread name: ",current_thread().getName())
# current_thread().setName("Linux")
# print("New Main thread name: ",current_thread().getName())

# Name() function
# from threading import Thread , current_thread
# def disp():
#     print("Child: ",current_thread().name)    
# t = Thread(target=disp)
# t.start()
# print("Main: ",current_thread().name)

# Setting name by Name() function

# from threading import Thread , current_thread
# def disp():
#     print("Default Child: ",current_thread().name)  
#     current_thread().name = "Flying Thread"  
#     print("New Child: ",current_thread().name)  
# t = Thread(target=disp)
# t.start()
# print("Default Main: ",current_thread().name)
# current_thread().name = "Hacker"
# print("New Main: ",current_thread().name)

# Outside a function:
# Using is_alive

from threading import Thread , current_thread
def disp():
    pass
t = Thread(target=disp)
print(t.getName())
t.setName("Hacker")
print(t.getName()) 
print(t.is_alive())