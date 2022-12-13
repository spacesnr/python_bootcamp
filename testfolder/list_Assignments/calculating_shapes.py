import math

#program that calculates diggerent shapes as inputted by users

#function that identifies each shape
def id_shape(shape):
    shape = shape.lower() #to make sure the words typed maches with the devs. no caps

    if(shape == "rectangle"):
        return rectangle_area()
    elif (shape == "circle"):
        return circle_area()
    elif (shape == "triangle"):
        return triangle_area()
    else:
        return "Enter a circle, rectangle or triangle"

def rectangle_area():
    while True:
        try:
            a = float(input("enter the length : "))
            b = float(input("enter the width : "))
            break
        except ValueError:
            print("please type in numbers for both fields")
    area = a*b
    print("{:.2f}".format(area))


def circle_area():
    while True:
        try:
            a = float(input("enter radius : "))
            break
        except ValueError:
            print("pleas type a number for radius")
    
    area = math.pi * (math.pow(a,2))
    print("{:.2f}".format(area))


def triangle_area():
    while True:
        try:
            a = float(input("please enter the value for base : "))
            b = float(input("please enter the value for height : "))
            break
        except ValueError:
            print("please enter a number")
    area = 1/2 *a*b
    print("{:.2f}".format(area))

def main():
    chosen_shape = input("Enter a shape to calculate its area : ")
    print(id_shape(chosen_shape))

main()