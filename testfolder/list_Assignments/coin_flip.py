#Write a program that displays the num of heads & tails from a coin tossed 100 times

import random

coin_list = []

for i in range(1,101):
    coin_list += random.choice(["H","T","z"])


print("Heads :", coin_list.count("H"))
print("Tails :", coin_list.count("T"))
print("Tails :", coin_list.count("z"))