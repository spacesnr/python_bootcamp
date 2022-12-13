
#Write a function that prints out all the integers of a list but in reverse order

a_list = [1,2,"4",3,4,5,3.8]

def list_fx(a):
    list = []
    for char in reversed(a):
        if(type(char) == int):
            list.append(char)
        else:
            continue
    print(list)
     
list_fx(a_list)




