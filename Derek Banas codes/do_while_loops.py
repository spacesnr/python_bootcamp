
"""# Do while loops does the task before checking if it has to do the task again (Makes use of while and break statement)

# A guessing game to demonstrate a Do While loop

secret_number = 7

while True:
    guess_number = int(input("Please enter a number 1-10 : "))
    if (secret_number == guess_number):
        print("You guessed it!")
        break

"""


# A guessing game to demonstrate a Do While loop with exception handling

secret_number = 7

while True:
   
    try:
        guess_number = int(input("Please enter a number 1-10 : "))
        if (guess_number == secret_number):
            print("You guessed it!")
            break
    except ValueError:
        print("Please enter a real number")
    except:
        print("unknown error")
 

