'''
Write a script that demonstrates a try/except/else.

'''

try:
    x, y = [int(x) for x in input("Enter two value: ").split()]
    z = x / y
except ZeroDivisionError:
    print("Divisor cannot be zero")
else:
    print(z)