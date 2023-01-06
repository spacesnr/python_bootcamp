#A game of rock, paper, scissors against the computer
import random


print("Please select 'Rock', 'Paper', or 'Scissors'")
print()
comp_choice = random.choice(["rock","paper","scissors"])

while True:
    user_choice = input("Enter your selection : ")
    user_choice = user_choice.lower()

    print("You picked {}, computer picked {}".format(user_choice,comp_choice))

#if statement to show when you win the game
    if user_choice == "rock" and comp_choice == "scissors":
        print("You win!")
        break
    elif user_choice == "scissors" and comp_choice == "paper":
        print("You Win!")
        break
    elif user_choice == "paper" and comp_choice == "rock":
        print("You Win!")
        break

#if statement to show when you lose the game
    if comp_choice == "rock" and user_choice == "scissors":
        print("You Lose!")
        break
    elif comp_choice == "scissors" and user_choice == "paper":
        print("You Lose!")
        break
    elif comp_choice == "paper" and user_choice == "rock":
        print("You Lose!")
        break


#if statement to show when theres a tie the game
    if user_choice == "rock" and comp_choice == "rock":
        print("A tie, play again")
        continue
    elif user_choice == "paper" and comp_choice == "paper":
        print("A tie, play again")
        continue
    elif user_choice == "scissors" and comp_choice == "scissors":
        print("A tie, play again")
        continue


