
class Faculty:
    def __init__(self):
        self.facname = "Engineering"
        self.type = "Science"
        self.HOD = "HOD"




class Students(Faculty):
    all = []
    def __init__(self,fname,lname):
        super().__init__()
    
        self.fname = fname
        self.lname = lname
        Students.all.append(self)

    

    def PrintName(self):
        print(f"{self.fname},{self.lname}")

emma = Students("ojukwu","emma")
joy = Students("juliet", "agu")


emma.PrintName()

print(emma.facname)