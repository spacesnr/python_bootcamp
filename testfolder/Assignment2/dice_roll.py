#A game to roll 2 dice, if you roll 12 you win a jackpot
import random

dice1 = random.randint(1,7)
dice2 = random.randint(1,7)

print("\nTo roll the two dice, type in ROLL")
print()

while True:
    user_choice = input("Please Roll dice : ")
    user_choice = user_choice.lower()

    if user_choice =="roll":
        if (dice1 + dice2)==12:
            print("Jackpot!!! You rolled 12!")
            break
        if (dice1 + dice2)!=12:
            print("You rolled {}".format(dice1 + dice2))
            #print(dice1,dice2)
            break
    
    else:
        print("\nPlease type ROLL")
        continue