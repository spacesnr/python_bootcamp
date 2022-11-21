# A simple program to convert miles to KM
# ask users to input a mile and store in variable miles
Miles = input("Enter mile: ")

#convert to interger
miles = int(miles)

# Convert mile to KM (note: 1 mile is 1.609KM ) and store as miles_KM
miles_KM = 1.609

# conversion value stored in converted
converted = miles * miles_KM

#print value
print(converted)
#or we can use ths;
print("{} miles equals {} kilometers".format(miles, converted))
