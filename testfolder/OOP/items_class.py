import csv

class item:
    pay_rate = 0.8 #This is a class attribute 
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        
        #Validating arguments (making sure they are not negative values)
        assert price >= 0, f"The price {price} is not equal or greater than zero"
        assert quantity >= 0, f"The quantity {quantity} is not equal or greater than zero"

        #Attributes Declaration
        self.__name = name
        self.price = price
        self.quantity = quantity

        #Appending to create a list
        item.all.append(self)

    @property #property decorators are used to declare attributes that cant be changed(read-only)
    def name(self):
        return self.__name #(putting double __ here and in the attribute declartion section is good practice for the readonly to wrk)

    @name.setter #This decorator is used when you still wish to change the name
    def name(self, value):
        if (len(value) > 10): #if you want to limit their character input
            raise Exception("Name too long!")
        else:
            self.__name = value

    def calulate_price(self):
        return self.price * self.quantity
    
    def discounted_price(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_class(cls):
        with open("items.csv","r") as f:
            reader = csv.DictReader(f)
            things = list(reader)
        for items in things:
            item(name=items.get("name"),
                 price=float(items.get("price")),
                 quantity=float(items.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        #We will count out floats that are point zero (ie: 6.0, 12.0,etc)
        if isinstance(num, float):
            #count out floats that are point zero
            return num.is_integer()
        elif(num, int):
            return True
        else:
            return False
        
    
    



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"