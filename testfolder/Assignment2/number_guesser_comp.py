#Select a number from 1-50 and let the computer guess your number
import random
comp_choice = random.randint(1,51)
user_choice = int(input("Please a number (1-50) : "))

if comp_choice == user_choice:
    print(f"The computer guessed correctly {comp_choice}!!")
else:
    print(f"You guessed {user_choice}, computer guessed {comp_choice}")
