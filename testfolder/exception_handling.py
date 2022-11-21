"""
## How to handle errors from displaying on the terminal
while True:
    try:
        name1 = int(input("Enter a number : "))
        break
    except ValueError: #Used to check if u have a value error (ie; you entered a wrong value)
        print("You didnt enter a number")
    except: # used to account for any other error that might occur
        print("unknown error")
print("Thankyou")

"""


##Do while loop (makes you of the True and break statements)
## A simple guessing game

secret_n = 44
while True:
    guess = int(input("enter a evalue : "))
    if (guess == secret_n):
        print("You guessed it!")
        break
    


    
"""
## How to make an acronym
user_input = input("Enter a word for acronym : ")
user_input = user_input.upper()
user_input = user_input.split() #This is how to convert a string to a list using .split()

for i in user_input:
    print(i[0], end="")
    
print()

"""