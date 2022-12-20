#generate a radom list of numbers from 1-1000 in a range of 100 values then print multiples of 9 in the range

import random

randlist = list(random.randint(1,1001) for i in range(1,101))
print(list(filter((lambda x: x % 9 == 0), randlist)))




    

