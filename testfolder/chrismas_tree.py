"""
#Building out a christmass tree with user input

tree_height = int(input("Enter your tree height: "))
#spaces increase by 1
# Hashes increase by 2
hashes = 1
tree_spacing = tree_height - 1
stump = tree_height - 1

while (tree_height != 0):
    for i in range(tree_spacing):
        print(" ", end="")
    for i in range(hashes):
        print("#", end="")
    print()
    tree_spacing -= 1
    hashes += 2
    tree_height -= 1
for r in range(stump):
    print(" ", end="")
print("#")

"""

## Building out a guessing game (Guess the secret number)

secret_number = 10

while True:
    guess = int(input("Guess a lucky number: "))
    if guess == secret_number:
        print("you guessed it!!")
        break
    

