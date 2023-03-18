def emeka(x):
    emeka.counter = getattr(emeka, "counter", 5) +1
    #return 4

for x in range(10):
    emeka(x)
print(emeka.counter)