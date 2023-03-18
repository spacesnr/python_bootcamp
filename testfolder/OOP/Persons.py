#

class Person:

    def __init__(self,names):
        self.name = names

    def introduce(self):
        print(f"hello, {self.name}")

emma = Person("charles")
emma.age = 5
emma.introduce()
print(emma.__dict__)
