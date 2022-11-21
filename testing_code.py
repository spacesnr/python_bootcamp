# students to input their age and store value in age
age = eval(input("enter age "))

# age 5 goes to kindergatin
if (age == 5):
    print("Go to kindergatin")
 
# age 6 to 17 goes to grade 1 through 7
elif (age >=6) and (age <=17):
    print("Go to grade 1 to 7")

# age 18 goes to colledge
elif (age >= 18):
    print("Go to colledge")
else:
    print("too young") 