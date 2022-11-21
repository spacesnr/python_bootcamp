#collect input from users and store in varable num1, num2
num1, num2 = input("Enter two numbers " ).split()
#convert numbers to interger
num1 = int(num1)
num2 = int(num2)
#add values and store in sum
sum = num1 + num2
#print result
print("{} + {} = {}".format(num1, num2, sum))
