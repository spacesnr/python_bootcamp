from items_class import item
from phone_class import phone

#item.instantiate_class()
item1 = item("cup", 5000, 8)
item2 = item("laptop",700, 10)

print(item.calulate_price(item2))

print(item2.name)