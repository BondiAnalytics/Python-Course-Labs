'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
try:
    x, y = [int(x) for x in input("Enter two value: ").split()]
    z = x / y
    print(z)
except ZeroDivisionError:
    print("Divisor cannot be zero")