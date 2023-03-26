"""A class to create Robots"""

#def introduce():
   # print(f"\nhi i'm {x.name} \n")

class Robot:
   def __init__(self, color="black",func="maths genuis"):
      self.color = color
      self.func = func

   def introduce(self):
      if self.name:
         print(f"hi, welcome {self.name}, you are a {self.gender} !")
      else:
         print("child!")
      
      #  self.obj = obj
       # print(f"\nhi i'm {obj.name} \n")

   def setGender(self,gender):
      self.gender = gender
      
   def getGender(self):
      return self.gender
   

x = Robot()
y = Robot()
z = Robot("yellow", "cooking")
Robot.brand = "Starline"
x.name = "ElonX"
y.name = "stargate"

y.setGender("male")
x.setGender(y.getGender())



x.buildYear = 1993
y.buildYear = 2000

#def introduce():
#    print(f"\nhi i'm {y.name} \n")

print(f"\n{type(x).getGender(x)}\n")

#Robot.introduce(y)
y.introduce()
x.introduce()
#type(z).introduce(x)





