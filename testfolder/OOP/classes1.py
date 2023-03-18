
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name},({self.age})"
        
    def myfunc(self):
        print("My name is " + self.name)



p1 = person("max", 32)
print(p1)
p1.myfunc()

p1.age = 40 #object properties canbe modified
#del p1.age #object properties canbe deleted
#del p1 #objects can be deleted
print(p1.age)


#NOTE: class definitions can't be empty, but if for some reason u have a class definition with no content, put in the pass statement to avoid getting an error.