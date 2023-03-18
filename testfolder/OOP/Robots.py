"""A class to create Robots"""

class Robot:
    def __init__(self, color="black",func="maths genuis"):
        self.color = color
        self.func = func

x = Robot()
y = Robot()
z = Robot("yellow", "cooking")
Robot.brand = "Starline"
x.name = "ElonX"
y.name = "stargate"
getattr(x, "country","USA")

x.buildYear = 1993
y.buildYear = 2000

print(f"\n{x.country}\n")

#getattr 
