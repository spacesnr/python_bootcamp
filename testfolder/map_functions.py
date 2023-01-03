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
