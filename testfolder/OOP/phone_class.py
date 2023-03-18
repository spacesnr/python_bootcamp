from items_class import item

class phone(item):
    
    def __init__(self,name:str, price:float, quantity:int,broken_phone=0):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_phone
        assert broken_phone >= 0, f"broken phone {broken_phone} isnt greater or equal to zero"

phone1 = phone("samsung", 1000, 8, 0)
