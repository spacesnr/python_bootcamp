from functools import reduce
#Program using reduce for factorial

def fac(n,y=1):
    
    if  (n==0 or n==1):
        return y
    else:
        return n*fac(n-1)

print(reduce(fac,[5,0]))
