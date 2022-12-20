#A splat operator is used when we dont know the number of arguments that will be passed to a function

def sumAll(*arg):
    sum = 0

    for i in arg:
        sum += i
    return sum
print(sumAll(1,2,3,4,5))