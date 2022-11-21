var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

for xx in var_list:
    if(1 <= xx <=5):
        print(xx)
    elif(8 <= xx <= 10):
        print(xx, end=":\n")
    else:
        print("invalid")
  

  
  #  print(xx, end=": ")

'''assignment: print numbers 1-20, multiples of 3 will be replcesd by Fizz 
and multiples of 5 will be replaced by Buzz. multiples of 3 and 5 will be replaced by FizzBuzz'''
"""
var_assign = range(1,21)

for var_input in var_assign:
    if((var_input % 3 == 0) and (var_input % 5 != 0)):
        print("\n Fizz")

    elif((var_input % 5 == 0) and (var_input % 3 != 0)):
        print("\n Buzz")

    elif(var_input % 3 == 0) and (var_input % 5 == 0):
        print("\n FizzBuzz")
        
    else:
        print("\n", i)
"""

'''
var_assign = range(1,21)

for var_input in var_assign:
    if(var_input % 3 == 0) and (var_input % 5 == 0):
        print("\n FizzBuzz")
    elif(var_input % 5 == 0):
        print("\n Buzz")
    elif(var_input % 3 == 0):
        print("\n Fizz")  
    else:
        print("\n", i)
'''
"""
# netted IFs

var_num = range(1, 61)
var_input = int(input("Please enter a number 1-60: "))
if(var_input in var_num):
   # for var_input in var_num:
    if(var_input < 20):
        if(var_input % 2 == 0):
            print("EVEN")
        else:
            print("ODD")
    elif(20 < var_input < 40):
        if(var_input % 3 == 0):
            print("Fizz")
        elif(var_input % 5 == 0):
            print("Buzz")
        else:
            print(var_input)
    else:
        if(40 < var_input < 50):
            print("Yes")
        elif (50 < var_input < 60):
            print("No")
else:
    print("Number is out of range!")
"""