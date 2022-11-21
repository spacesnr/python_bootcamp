
from math import factorial
"""
n = int(input("Enter a number: "))
def rec(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(rec(n))
"""

"""

n = int(input("Enter a number: "))    
def fac(n):
    if(n==0 or n==1):
        return 1
    else:
      return n*fac(n-1)
print(fac(n))
"""
"""
#code in progress: still working on the code
#0,1,1,2,3,5,8,13,21,34
#n = 5
def fib1(n=7):
 #   a = 0
 #   b = 1
    a, b = 0, 1
    for i in range(n+1):
        print(a, end="")
        sum = a+b
        a = b
        b = sum
    #    a, b = b, a+b
        print("")

fib1(5)
"""

n = int(input("enter a number: "))
def fib(n):    # write Fibonacci series up to n with a while loop
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(n)    


