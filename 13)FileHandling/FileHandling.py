# Files are named locations on disk to store related information.
#  They are used to permanently store data in a non-volatile
#   memory (e.g. hard disk).

# In Python, a file operation takes place in the following order:

# --Open a file
# --Read or write (perform operation)
# --Close the file

#--------------------------------------------------------
# Opening Files in Python
#---------------------------------------------------------
# Python has a built-in open() function to open a file.
#  This function returns a file object

f = open("test.txt")    # open file in current directory
f = open("C:/Python38/README.txt")  # specifying full path

# We can specify the mode while opening a file. In mode, we 
# specify whether we want to read r, write w or append a to the
#  file. We can also specify if we want to open the file in 
#  text mode or binary mode.



# Mode      	Description
#------------------------------------------------------------------
# r     	Opens a file for reading. (default)
# w	        Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x	        Opens a file for exclusive creation. If the file already exists, the operation fails.
# a	        Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t	        Opens in text mode. (default)
# b	        Opens in binary mode.
# +	        Opens a file for updating (reading and writing)

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

#--------------------------------------------------------------
# Closing Files in Python
#--------------------------------------------------------
# When we are done with performing operations on the file,
#  we need to properly close the file.
#  It is done using the close() method available
#  in Python.

f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()

# This method is not entirely safe. If an exception occurs when we are performing some operation with the file,
#  the code exits without closing the file.

# A safer way is to use a try...finally block.

try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

#--------------------------------------------------------------
# Writing to Files in Python
#------------------------------------------------------------
# In order to write into a file in Python, we need to open it in
#  write w, append a or exclusive creation x mode.


# Writing a string or sequence of bytes (for binary files) is 
# done using the write() method.

f=open("test.txt",'w')

f.write("Hello Rohit Your file is opened and data is written successfully")

# This program will create a new file named test.txt 
# in the current directory if it does not exist.
#  If it does exist, it is overwritten.

f=open("test.txt",'a')
f.write("\nThankyou")

# This program will create a new file named test.txt 
# in the current directory if it does not exist.
#  If it does exist, data will be appended to it.

# Reading Files in Python
#-----------------------------------------------------------
# To read a file in Python, we must open the file in reading r mode.


f=open("test.txt",r)
f.read()



# We can change our current file cursor (position) using the
#  seek() method. Similarly, the tell() method returns our 
#  current position (in number of bytes).
f.tell()   # # get the current file position
f.seek()   # bring file cursor to initial position

# We can read a file line-by-line using a for loop. 
# This is both efficient and fast.

for line in f:
    print(line,end=' ')

#In this program, the lines in the file itself include a 
# newline character \n. So, we use the end parameter 
# of the print() function to avoid two newlines when printing.


# Alternatively, we can use the readline() method to read
#  individual lines of a file. This method reads a file 
#  till the newline, including the newline character.

f.readline()


#  Lastly, the readlines() method returns a list of remaining
#   lines of the entire file. All these reading methods return
#    empty values when the end of file (EOF) is reached.

f.readlines()

