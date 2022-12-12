#write a function that displays all the integers in a list. The list is the argument of the function

a_list = [1,2,"4",3,4,5,3.8]

def list_fx(a):
    for char in a:
        if(type(char) == int):
            print(char, end=" ")
        elif(type(char)== str):
            print("{}s".format(char), end=" ")
        else:
            print("\ni dont recognise this character")
list_fx(a_list)


