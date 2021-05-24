'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

n = int(input("Input number between 1 and 1,000,000,000: ", ))

def number_fun(n):
    if n % 4 == 0 or n % 7 == 0:
        return True
    else:
        return False

print(number_fun(n))