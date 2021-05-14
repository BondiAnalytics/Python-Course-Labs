'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

Invest = float(input("Investment amount ", ))
Rate = float(input("Investment rate ", ))
Years = float(input("Investment years ", ))
print(Invest * (1 + Rate) ** Years)