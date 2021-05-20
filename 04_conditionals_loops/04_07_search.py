'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

n = int(input("Provide a number between 1 and 1,000,000,000: ", ))

guess = 0

while guess < 1000000000:
    guess += 1
    if guess == n:
        break
print(guess)