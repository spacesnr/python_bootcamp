

#Write a function to solve the equation x + 5 = 9

def solve_eqn(equation):
    #split the input into variables
    x, add_sign, num1, eql_sign, num2 = equation.split()

    #convert numbers into intergers
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2-num1) #convert back to strings inorder to concantenate
print(solve_eqn("x + 5 = 9"))


"""
#equation x + 5 = 9, 5 + x = 9

def solve_eqn(equation):
    #split the input into variables
    x, add_sign, num1, eql_sign, num2 = equation.split()

    #convert numbers into intergers
    if():
        num1, num2 = int(num1), int(num2)
        return "x = " + str(num2-num1) #convert back to strings inorder to concantenate
    else:
        return "sad!"
print(solve_eqn("4 + x = 9"))
"""