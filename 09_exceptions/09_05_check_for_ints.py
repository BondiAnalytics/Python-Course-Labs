'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

try:
    nmbr = int(input("Enter a number: ", ))
except ValueError as error:
    print("Please enter a number")
    nmbr = int(input("Please retry: ", ))
    print(f"Thank you for entering {nmbr}")