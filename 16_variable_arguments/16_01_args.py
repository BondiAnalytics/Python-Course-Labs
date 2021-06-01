'''
Write a script with a function that demonstrates the use of *args.

'''

def races(*args):
    for i in args:
        print(i)

races('All-Comers', 'Club Northwest', 'Bloomsday')