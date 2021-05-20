'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5

c = 0
a = []
while c < n:
    a.append("*")
    print(a)
    c += 1