'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

Numbers less that 1111, because we want remainders equal to zero.

'''


# import random
# randomlist = []
# for i in range(0,1000):
#     i = random.randint(1000,6111)
#     randomlist.append(i)
#     #print(randomlist)
#
# gen = (i for i in randomlist if i // 1111 == 0)


# my_list = ["apple", "banana", "orange"]
#
# list = []
# for i, c in enumerate(my_list):
#     tup = i, c
#     list.append(tup)
# print(list)

def my_function(**kwargs):
    for i, k in kwargs.items():
        print(i, k)

my_function(item1='hi', item2='hello')