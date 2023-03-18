# printing random numbers into a list
import random

randlist = []

for i in range(5):
    randlist.append(random.randint(1,10))

i = len(randlist)-1

while i > 1:
    j = 0
    while j < i:
        print(f"\nIs {randlist[j]} > {randlist[j+1]}")
        if randlist[j] > randlist[j+1]:
            print("Switch")
            temp = randlist[j]
            randlist[j] = randlist[j+1]
            randlist[j+1] = temp
        else:
            print("Dont switch")
        j += 1
        for k in randlist:
            print(k, end=", ")
        print()
    print("End of round")
    i -= 1
for i in randlist:
    print(i, end=", ")    
print()