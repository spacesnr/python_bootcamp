
import random

result = {
    "rock":{"rock":"draw","paper":"player lost","scissors":"player wins"},
    "paper":{"paper":"draw","scissors":"player lost","rock":"player wins"},
    "scissors":{"scissors":"draw","rock":"player lost","paper":"player wins"}
    }

player_moves = {"r":"rock","p":"paper","s":"scissors"}
comp_moves = ["rock","paper","scissors"]

print("Lets play:'r' for 'rock', 's' for 'scissors','p' for 'paper' & 'CTL C' to exit game")
player_input = input("pick an option : ").lower()

while player_input != "c":
    comp_choice = random.choice(comp_moves)
    player_choice = player_moves[player_input]
    print("you chose: ",player_choice,"computer chose:",comp_choice)
    print(result[player_choice][comp_choice])

    player_input = input("pick an option : ").lower()