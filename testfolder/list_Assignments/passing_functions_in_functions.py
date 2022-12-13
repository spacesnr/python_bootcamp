#write a code that prints out odd nums in a list

#function that checks for odd nums
def check_odd(num):
    if (num % 2 == 0):
        return False
    else:
        return True

def listCheck(list, func):
    odd_list = []
    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list

a_list = [1,2,3,4,5,6,7,8,9,10]
print(listCheck(a_list,check_odd))
    
