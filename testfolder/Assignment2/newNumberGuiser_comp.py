import random

count = 0

a=True
user_num = 0
print("Welcome to a guessing game")



while True:
    try:
        user_num = int(input("Please select a number (1-50) : "))
        if user_num > 50:
            print("limited passed")
            continue
        else:
            break    
        break
        
    except ValueError:
        print("Select a number nyash!")
    except:
        print("Select an actaul number dummy!")
       
comp_num = random.randint(1,51)
while a != False:
    count += 1
    print(f"computer chose {comp_num}")

    if user_num != comp_num:
            
        user_input = str(input("Is comp choice Higher(H) or lower(L)? : ")).lower()
        print()
        if user_input == "h":
            comp_num = comp_num - random.randint(1,2)
        elif user_input == "l":
            comp_num = comp_num + random.randint(1,2)
        elif user_num == comp_num:
            print(f"odogu, you tried {count} times")
            break
        elif user_input != "h" or user_input != "l":
            print("select either 'H' or 'L'")
            continue

   


                