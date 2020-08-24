# A thread is basically an independent flow of execution.
#  A single process can consist of multiple threads. Each
#   thread in a program performs a particular task.
#  multithreading can be used only when the dependency between
#   individual threads does not exist.

# How to achieve Multithreading in Python?
#-------------------------------------------------------------
# Multithreading in Python can be achieved by importing the 
# threading module.


from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)
he=Hello()
hi=Hii()


he.start()
sleep(0.2)
hi.start()

he.join()
hi.join()
print("Finished")
