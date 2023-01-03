#A game to guess a computer generated number between 1-50. Correct guess wins a jackpot. Max attempt 3

import random

a=0

while a != 3:
    comp_num = random.randint(1,51)
    user_num = int(input("Select a number (1-5) : "))
    if comp_num != user_num:
        print("You lost. Computer selected {}".format(comp_num))
        print("\n You have {} more attempts".format(2-a))
        a += 1
    else:
        print("Jackpot!!! You won!")
                