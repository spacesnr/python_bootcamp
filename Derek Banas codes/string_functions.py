
rand_string = "   this is very important  "

rand_string = rand_string.lstrip() #strips the white spaces on the left
rand_string = rand_string.rstrip() #strips the white spaces on the right
rand_string = rand_string.strip() #strips the white spaces on both sides

print(rand_string)

print(rand_string.capitalize()) #capitalizes the first word in the string
print(rand_string.upper()) #converts the string to upper case
print(rand_string.lower()) #converts the string to lower case


#converting a list to a string
a_list = ["a", "bunch", "of", "words"]
print(" ".join(a_list)) # " " indicates it will be separated by a space and .join() is the function


#converting strings to lists
a_string = rand_string.split()
for i in a_string:
    print(i)


#counting the number of a perticular word in a string
print("How many 'is' is there in this string? : ", rand_string.count("is"))

#Finding the position of a word in a string
print("The word important starts at index : ", rand_string.find("important"))

#replace word(s) in a string
print(rand_string.replace("very ", "kinda "))




a_letter = "z"
num_3 = "3"
a_space = " "

print("Is a_letter a number or letter : ", a_letter.isalnum())
print("Is a_letter a letter : ", a_letter.isalpha())
print("Is num_3 a number : ", num_3.isdigit())
print("Is a_letter a lowercase : ", a_letter.islower())
print("Is a_letter an uppercase : ", a_letter.isupper())
print("Is space a space : ", a_space.isspace())





"""
#Acronym generator: lets people type in word and you make an acronym of it

rand_word = input("Enter a string : ")
rand_word = rand_word.upper()

for i in rand_word.split():
    print(i[0], end="")
"""