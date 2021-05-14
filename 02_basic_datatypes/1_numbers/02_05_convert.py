'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

integer = 10
fl = float(integer)
integer = int(fl)
# floor_division =  / int #what is floor division?

u1 = int(input("First input:", ))
u2 = int(input("Second input: ", ))
print(u1 * u2)