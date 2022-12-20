# for unicodes A-Z = 65 - 90
# a-z = 97 - 122

# convert letters to characters using ord()
# convert characters back to letters using chr()

#example of using unicode: take an input in uppercase, then print out "secret mssg" then convert back and print original message

random_input = input("Enter a message to hide in upper case : ")
random_input2 = random_input.upper() #conver to upper case, just incase the user didnt type in uppercase

secret_msg =""

#cycle through character and store their conversion
for i in random_input2: 
    secret_msg += str(ord(i)) # to make the code wrk for lowercase, use str(ord(i) -23)
print("Secret message : ", secret_msg)

og_msg = ""

#cycle through the characters in twos
#Then create a var that will hold the first 2 digits
#finally store the converted characters 

for i in range(0, len(secret_msg)-1, 2):
    char = secret_msg[i] + secret_msg[i+1]
    og_msg += chr(int(char)) # to make the code wrk for lowercase, use chr(int(char) +23)
print("Original message : ", og_msg)
















"""
sample_string = "This is a very import message"
for i in range (0, len(sample_string)-1, 2):
    print(sample_string[i] + sample_string[i+1])
"""