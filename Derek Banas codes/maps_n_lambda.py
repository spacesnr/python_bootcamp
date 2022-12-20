#MAPS allow us to execute a function on each item of a list

a_list = range(1,11)

def func(num):
    return num * 2

print(list(map(func, a_list)))


#Same result but written without the use of Map. Map prints same result with just one line of code.
#maps can be used instead of for loops to print or work on lists or both!
a = []
for i in a_list:
    a.append(func(i))
print(a)



#Meanwhile lambda are nameless functions

sum = lambda x,y: x+y
print(sum(3,3))

#re-writing the map function above using lambda as a function
print(list(map((lambda x: x*2),a_list)))


#filter() function
print(list(filter((lambda x: x % 2==0), range(1,11)))) #filters n only prints the even nums



#In order to use the reduce function, you'll have to import it
#Also the reduce function converts a list to a single character
from functools import reduce
print(reduce((lambda x,y: x+y), range(1,6)))

main = lambda x,y: x if (x>y) else y 
print(reduce(main, [20,4,1,11,33,6,3]))
