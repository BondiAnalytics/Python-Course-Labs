'''
Print out every prime number between 1 and 100.

'''

for n in range(1,10000):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and n % 11 != 0:
        print(n)