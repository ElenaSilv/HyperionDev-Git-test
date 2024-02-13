# The program allows the user to calculate their investment interest (either simple or compound)
# OR to calculate a home loan repayment plan. 

import math

options ='''
Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a loan
'''

print(options)

investment = "investment"
bond = "bond"

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

simple_interest = "simple"
compound_interest = "compound"

# Investment calculator 

if user_choice == investment:
    deposit = int(input("How much money do you want to deposit? ")) 
    interest_percentage = int(input("Please tell us the percentage of the interest rate (no symbols): "))/100
    years = int(input("How many years do you plan on investing? "))
    interest = input("Do you want a simple or compound interest? ").lower()

    if interest == simple_interest:
        print(deposit *(1+interest_percentage*years))
    elif interest == compound_interest:
        print(deposit * math.pow((1+interest_percentage),years))
    else:
        print("Please start again and choose either 'simple' or 'compound.")
