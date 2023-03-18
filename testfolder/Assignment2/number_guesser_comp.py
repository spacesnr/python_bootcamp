#Select a number from 1-50 and let the computer guess your number
import random
comp_choice = random.randint(1,50) #randint() is different from randrang() because randint() will include the last value (50) but rndrang() will stop at the value before the last digit.
user_choice = int(input("Please a number (1-50) : "))

if comp_choice == user_choice:
    print(f"The computer guessed correctly {comp_choice}!!")
else:
    print(f"You guessed {user_choice}, computer guessed {comp_choice}")
