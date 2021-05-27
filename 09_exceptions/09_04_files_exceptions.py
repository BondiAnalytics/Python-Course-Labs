'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

with open("war_and_peace.txt", "r") as fin:
    wnp = fin.read()
print(wnp[0:100])

with open("crime_and_punishment.txt", "r") as fin:
    cnp = fin.read()
for i in cnp:
    i = ""

try:
    print(wnp[0])
    print(cnp[0])
    print(pnp[0])
except NameError as error:
    print("Book is not loaded")

'''

Need help on this one!!

print("BONUS CHALLENGE")

class princeerror(Exception):
    def __init__(self, prince):
        self.prince = prince



try:
    wnp_list = wnp.split()
    cnp_list = cnp.split()
    pnp_list = pnp.split()

    prince = int(wnp[])
    print(wnp)

    print(cnp)
    print(pnp)
except
'''