import random

count = 0

a=True
comp_num = random.randint(1,51)
print("Welcome to a guessing game")
while a != False:
    
    try:
        user_num = int(input("Please select a number (1-51) : "))
        
        count += 1
        if comp_num != user_num and user_num > comp_num:
            print(f"your number is higher than computers \n")
        
        elif comp_num != user_num and user_num < comp_num:
            print(f"your number is lower than computers \n")  
        elif comp_num == user_num:
            print(f"jackpot, you guessed {count} times \n")
            break

    except ValueError:
        print("select a number nyash!")
    except:
        print("Slect an actual number dummy!")

        if user_num > 50:
            print("You exceeded the limit")
