'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

n = int(input("Enter a patient's age: ", ))

new_ages = [50,20,40,50,10,34,50,38,39,21,23,26,40,20]
# ave_age = int(sum(ages) / len(ages))
# print(ave_age)

def ave_age(ages):
    av_age = int(sum(ages) / len(ages))
    return av_age

def eligible_age(n):
    if n > ave_age(new_ages):
        vaccinated = str(input("Are you already vaccinated? (Yes or No): ", ))
        return vaccinated.lower
    else:
        return print("You are too young")

def eligible_vaccinated(n):
    if eligible_age(n) == "no":
        return "Please proceed to the nearest vaccination clinic."
    else:
        return "You don't need a vaccincation at this point."

print(eligible_vaccinated(n))