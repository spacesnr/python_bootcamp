import random
#from words import word_list

def HangmanGame():

    words = random.choice(["apple"])
    spaces = len(words)
    tries = 6
    dashes = "_" * spaces
    guessedLetters = []
    guessedCorrect = 0

    print("\nWelcome to the Hangman Game. Guess a fruit")

    while guessedCorrect == 0 and tries > 0:
        user_input = str(input("\nEnter a word or letter : ")) # taking user input

        if len(user_input) == 1 and user_input.isalpha(): 
            if user_input in words:
                guessedLetters.append(user_input)
                listdashes = list(dashes)
                index = [i for i, r in enumerate(words) if r == user_input] # to get the index of each user input
                
                for x in index:
                    listdashes[x] = user_input #Placing the user input on the right dashes
                    dashes = "".join(listdashes)
                
                if "_" not in dashes:
                    #print("yes!!!")
                    guessedCorrect = 1
            #    print(f"You already guessed {user_input}")
            else:
                #prints when you guessed a wrong letter
                print("You guessed a wrong letter")
                tries -= 1
                guessedLetters.append(user_input)
        elif len(user_input) == len(words): #When a user types in an entire word
            
            if user_input == words:
                #print(f"\nCongratulations, you guessed {user_input} correctly\n")
                guessedLetters.append(user_input)
                guessedCorrect = 1
                dashes = words
            else: 
                print("\nYou guessed wrongly\n")
                tries -= 1
                guessedLetters.append(user_input)
        else:
            print("\nYou guessed the wrong word\n")
            tries -= 1
            guessedLetters.append(user_input)

        print()
        print(dashes)  
        print(f"You have {tries} tries remaining and u've gussed : " + ", ".join(guessedLetters))

    if guessedCorrect == 0:
        print("\nOh no, You couldnt save Morty!\n")
    else:
        print("\nCongratulations, Morty lives because of you!\n")

def main():
    HangmanGame()
    while input("Do you wish to play again?(Y/N) : \n").upper() == "Y":
        HangmanGame()
    print("Bye, see you soon")

main()












