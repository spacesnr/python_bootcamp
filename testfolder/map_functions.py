#A program to display the fibonacci series
from functools import reduce


def fib(a,b):
    a = 0
    b = 1
    while a < 100:
        print(a, end=" ")
        a,b = b, a+b
    print()

print(reduce(fib, [0,1]))


def fac(n,y):
    y = 1
    if  (n==0 or n==1):
        return y
    else:
        return n*fac(n-1)
print(fac(5,1))

#print(reduce(fac,[5,1]))
