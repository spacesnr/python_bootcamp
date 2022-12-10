#write a function that displays all the integers in a list. The list is the argument of the function
"""
a_list = [1,2,3,4,5,"b"]

def list_fx(a):
    for char in a:
        if(char==int(char)):
            print(char, end=" ")
        else:
            return
list_fx(a_list)
"""


#Write a function that prints out all the integers of a list but in reverse order

a_list = [1,2,3,4,5,7.3,"b"]

"""
def list_fx(a):
    for char in a:
        if(char==int(char)):
            print(char, end=" ")
        else:
            return
    
list_fx(a_list)

"""

#write a function that checks if its an integer
aa=""
def checkInt(a):
    if(aa.isdigit()):
        print("nyash")
    else:
        return False
vv=4
checkInt(vv)