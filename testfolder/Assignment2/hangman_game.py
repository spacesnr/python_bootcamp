import random

print("Welcome to the Hangman Game. Guess a fruit")

words = random.choice(["apple"])
spaces = len(words)
dashes = []

def printDashes(i):
    i = 0
    while i < spaces:
        dashes.append("_")
        i +=1


def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    
    while True:
        
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at=loc
    return print(locs)

        

user_input = str(input("Write an alphabet : "))
if user_input in words:
    print("ok na")
    rr = words.index(user_input)
    jj = words[rr]
    printDashes(spaces)
    list_duplicates_of(words, user_input)
    
    #dashes[rr] = user_input
    
    #print(" ".join(dashes))
    
else:
    print("hmmmm")






