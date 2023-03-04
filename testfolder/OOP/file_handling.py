"""
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist. Appends to the end of the file

"w" - Write - Opens a file for writing, creates the file if it does not exist. Over writes existing content

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""


f = open("pythonFile2.txt", "r")
print(f.read()) #read() used to read the doc, readline(); used to read only one line in the doc. Also you can specify the number of characters to read eg: read(8)
f.close()

f= open("pythonFile2.txt", "a")
f.write("Adding more lines to the docs")
f.close()


f= open("pythonFile2.txt", "w")
f.write("RE-write the entire thing!!")
f.close()

#How to create a file
f = open("creatFile.txt", "x") #this creates a new file
f = open("creatFile.txt","w") #this also creates a new file if it doesnt exist & writes to it


#How to delete a file (First u'll have to import the OS module)
import os
os.remove("creatFile.txt")

#its adviced you check if the file exists before removing to avoid errors
if os.path.exists("creatFile.txt"):
    os.remove("creatFile.txt")
else:
    print("File doesnt exist")

#Deleting Folders
os.rmdir("myFolder") #note, you can only remove empty folders


