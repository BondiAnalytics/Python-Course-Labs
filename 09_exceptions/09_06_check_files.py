'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

try:
    with open('integers.txt', "r") as fin:
        file_name = fin.read()
        file_name = file_name.rstrip()
    # print(file_name)
    fn_int = int(file_name[0])
    calc = fn_int * 2500
    print(calc)
except ValueError as error:
    print("lovin' these datatype rules!!")
