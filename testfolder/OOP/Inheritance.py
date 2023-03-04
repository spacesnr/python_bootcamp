class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname,self.lname)
    
x = person("john","Agu")
x.printName()


#child class
class student(person):
    def __init__(self, fname,lname,year): #you can add an extra argument "year", the rest will be inherited from parent
        super().__init__(fname,lname) #instead of using pass, this automatically inherits the parents __init__ function 
        self.gradyear = year

    def welcomeMsg(self):
        print(f"Welcome, {self.fname} {self.lname}, to the class of {self.gradyear}")

y = student("Emeka","Nwagu", 2019)
print(y.gradyear)
y.printName()
y.welcomeMsg()