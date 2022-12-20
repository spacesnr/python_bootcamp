#How to handle exceptions (We use while loop and break statements)
"""
while True:
    try:
        var_input = int(input("Please enter a number: "))
        print(var_input)
        break
    except (KeyboardInterrupt):
        print("You didnt enter a number")
    except:
        print("unknown error")
print("\n Thankyou for entering a number \n")




#types of exception errors

1. value error
2. index error
3. name error
4. syntax error
5. keyboard interrupt (eg: ctl c to stop a running code)
6. type error


try:
    raise Exception("emeka", "jude")
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x = inst.args[0]
    y = inst.args[1]

    print("x = {}, \ny = {}".format(x,y))





import sys

try:
    x = open("myfile.txt")
    y = x.readline()
    z = int(y.strip())
    print(z)
except OSError as emma:
    print("OS error : {}".format(emma))
except ValueError:
    print("value cant be converted to int")
except BaseException as ike:
    print("unexpected error {}".format(ike))



def emma():
    x = 5/0
try:
    emma()
except ZeroDivisionError as err:
    print("the handling runtime error : {}".format(err))



#raising errors

try:
    raise NameError("hello there")
except NameError:
    print("This exception alredy exists")
   


#exception chaining
def main():
    raise ConnectionError
try:
    main()
except ConnectionError as comm:
    raise RuntimeError("failed to open DB") from None

"""

main = int(input("enter a number : "))
if type(main) != str:
    raise TypeError("must be an integer")







