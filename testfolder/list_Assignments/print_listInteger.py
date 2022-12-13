#write a function that displays all the integers in a list. The list is the argument of the function

a_list = [1,2,"4",3,4,5,3.8]

def list_fx(a):
    list = []
    for char in a:
        if(type(char) == int):
            list.append(char)
        else:
            continue
    return list
       
print(list_fx(a_list))



#Re-writing the same above code, but with 2 functions. One function taking a list & a function as arguments.
#function to check for integers
def check_integer(num):
    if type(num) == int:
        return True
    else:
        return False

#function to add integers to the list
def list_func(list, func):
    int_list = []

    for i in list:
        if func(i):
            int_list.append(i)
    return int_list

list = [1,2,"4",3,4,5,3.8]
print(list_func(list, check_integer))    

