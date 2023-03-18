import csv

class item:
    pay_rate = 0.8 #This is a class attribute 
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        
        #Validating arguments (making sure they are not negative values)
        assert price >= 0, f"The price {price} is not equal or greater than zero"
        assert quantity >= 0, f"The quantity {quantity} is not equal or greater than zero"

        #Attributes Declaration
        self.name = name
        self.price = price
        self.quantity = quantity

        #Appending to create a list
        item.all.append(self)

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
    

class phone(item):
    
    def __init__(self,name:str, price:float, quantity:int,broken_phone=0):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_phone
        assert broken_phone >= 0, f"broken phone {broken_phone} isnt greater or equal to zero"
        



item1=phone("lg", 400, 100, 4)
print(item1.calulate_price())
print(phone.all)
print(item.all)   
    
    
#item1 = item("phone", 1000, 5)

#item2 = item("laptop", 100, 3)

#item.instantiate_class()
#print(item.all)

#print(item.is_integer(8.6))

#item1.discounted_price()
#print(item1.price)

#item2.pay_rate = 0.7
#item2.discounted_price()
#print(item2.price)

"""
item1 = item("phone", 1000, 5)
item2 = item("laptop", 100, 3)
item3 = item("desk", 40, 80)
item4 = item("mouse", 26, 45)
item5 = item("cable", 20, 18)
"""




"""
class item:
    pay = 0.8 # 20% discount

    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Making sure you dont put negative numbers
        assert price >= 0, f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"


        self.name = name
        self.price = price
        self.quantity = quantity

        #Appending all instances to a list
        item.all.append(self)

    def calculate_totalPrice(self):
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.pay

    def __repr__(self):
        return f"item('{self.name},{self.price},{self.quantity}')"

item1 = item("phone", 1000, 6)
item1.discount()
print(item1.price)


item1.pay = 0.5
item1.discount()
print(item1.price)

item1 = item("phone", 1000, 6)
item2 = item("laptop", 600, 34)
item3 = item("watch", 560, 77)
item4 = item("headPhones", 800, 62)

print(item.all)
"""