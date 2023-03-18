
bolt_charges = [
    1200,2300,1800,1300,3000,1900,3300,1300,1700,2100,1600,1200,2200,1400,1700,1600,2800,1100,1600,
    1800,1900,1700,2800,1800,1600,600,4300,1100,700,900,700,1200,1700,2100,4200,1900,1300,1600,1500,
    3400,1000,1600,1700,1300,2000,700,2600,1100,1300,2300,1000,1400
]

total_cost = sum(bolt_charges)
print(total_cost)

total_ride = len(bolt_charges)
print(total_ride)

average_cost = total_cost/total_ride
print(average_cost)

def cost():
    