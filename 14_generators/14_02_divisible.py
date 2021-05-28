'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

import random
randomlist = []
for i in range(0,1000):
    i = random.randint(1000,6111)
    randomlist.append(i)
    #print(randomlist)



gen = (i for i in randomlist if i % 1111 == 0)

for i in gen:
    print(i)
