'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

nmbr = int(input("Input a number: ", ))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if nmbr <= 11:
    print(months[nmbr])
else:
    print("other")