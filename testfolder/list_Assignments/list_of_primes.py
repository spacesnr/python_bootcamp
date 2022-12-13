#Code that prints a list of primes when given a max number by thr user

#first we write a function to check for primes
def check_primes(num):
    for i in range(2,num): #range(2,num) makes it possible to start the count from 2 instead of 0
        if(num % 2)== 0:
            return False
        else:
            return True

#we write a function to add primes
def add_prime(num1):
    list_of_prime = []
    for i in range(2,num1):
        if(check_primes(i)):
            list_of_prime.append(i)
    return list_of_prime

user_prime = int(input("Enter a max prime : "))
print(add_prime(user_prime))